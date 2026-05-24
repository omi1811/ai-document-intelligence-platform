from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel): #client input
    username: str
    email: EmailStr
    password: str

class UserResponse(BaseModel): #client output/ client gets this response
    id: int
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel): #client input for login OR Requirements for Login
    email: EmailStr
    password: str

class Token(BaseModel): #client output for login OR JWT token response
    access_token: str
    token_type: str
