from pydantic import BaseModel, EmailStr

class AdminLoginRequest(BaseModel):
    email: EmailStr
    password: str

class AdminLoginResponse(BaseModel):
    access_token: str
    token_type: str
    user_type: str
    email: EmailStr
