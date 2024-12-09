from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    name: str
    role_id: int

class UserResponse(BaseModel):
    id: int
    name: str
    role_id: int

class RoleCreate(BaseModel):
    name: str

class PermissionCreate(BaseModel):
    name: str
    resource: str
    action: str

class AccessValidationRequest(BaseModel):
    user_id: int
    resource: str
    action: str