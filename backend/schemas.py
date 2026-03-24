from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    isbn: Optional[str] = None
    category: Optional[str] = None
    published_year: Optional[int] = None
    cover_image_url: Optional[str] = None
    file_url: Optional[str] = None
    is_available: bool = True

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    isbn: Optional[str] = None
    category: Optional[str] = None
    published_year: Optional[int] = None
    cover_image_url: Optional[str] = None
    file_url: Optional[str] = None
    is_available: Optional[bool] = None

class Book(BookBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class BorrowedBookBase(BaseModel):
    user_id: int
    book_id: int
    due_date: datetime

class BorrowedBookCreate(BorrowedBookBase):
    pass

class BorrowedBook(BorrowedBookBase):
    id: int
    borrowed_at: datetime
    returned_at: Optional[datetime] = None
    is_returned: bool = False
    
    class Config:
        from_attributes = True
