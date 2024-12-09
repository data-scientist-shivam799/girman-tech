from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import SessionLocal
from schemas.schemas import RoleCreate
from crud.role_crud import create_role, get_roles

router = APIRouter(prefix="/roles", tags=["Role Management"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_new_role(role: RoleCreate, db: Session = Depends(get_db)):
    return create_role(db, role)

@router.get("/")
def list_roles(db: Session = Depends(get_db)):
    return get_roles(db)