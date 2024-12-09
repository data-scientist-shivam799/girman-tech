from sqlalchemy.orm import Session
from models.models import Role
from schemas.schemas import RoleCreate

def create_role(db: Session, role: RoleCreate):
    db_role = Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def get_roles(db: Session):
    return db.query(Role).all()