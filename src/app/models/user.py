from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel): #client input
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel): #client output
    id: int
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

