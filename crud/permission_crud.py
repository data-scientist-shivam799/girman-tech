from sqlalchemy.orm import Session
from models.models import Permission
from schemas.schemas import PermissionCreate

def create_permission(db: Session, permission: PermissionCreate):
    db_permission = Permission(name=permission.name, resource=permission.resource, action=permission.action)
    db.add(db_permission)
    db.commit()
    db.refresh(db_permission)
    return db_permission

def get_permissions(db: Session):
    return db.query(Permission).all()