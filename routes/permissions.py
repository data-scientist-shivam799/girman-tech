from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import SessionLocal
from schemas.schemas import PermissionCreate
from crud.permission_crud import create_permission, get_permissions

router = APIRouter(prefix="/permissions", tags=["Permission Management"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_new_permission(permission: PermissionCreate, db: Session = Depends(get_db)):
    return create_permission(db, permission)

@router.get("/")
def list_permissions(db: Session = Depends(get_db)):
    return get_permissions(db)