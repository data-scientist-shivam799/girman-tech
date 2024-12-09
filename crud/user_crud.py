from sqlalchemy.orm import Session
from models.models import User
from schemas.schemas import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, role_id=user.role_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()