from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import SessionLocal
from models.models import User, Permission
from schemas.schemas import AccessValidationRequest

router = APIRouter(prefix="/validate-access", tags=["Access Validation"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def validate_access(request: AccessValidationRequest, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == request.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    permissions = user.role.permissions
    for permission in permissions:
        if permission.resource == request.resource and permission.action == request.action:
            return {"success": True, "message": "Access granted"}
    
    raise HTTPException(status_code=403, detail="Access denied")