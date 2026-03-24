import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
from models import Book, User, BorrowedBook
from schemas import Book as BookSchema, BookCreate, BookUpdate, User as UserSchema, UserCreate, BorrowedBook as BorrowedBookSchema, BorrowedBookCreate

app = FastAPI(title="Wonder Learning Digital Library API")

allowed_origins = os.getenv(
    "CORS_ORIGINS",
    "http://localhost:5173,http://127.0.0.1:5173,https://koshquest.in,https://www.koshquest.in",
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

allowed_hosts = os.getenv(
    "ALLOWED_HOSTS",
    "localhost,127.0.0.1,koshquest.in,www.koshquest.in",
).split(",")

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=allowed_hosts,
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Wonder Learning Digital Library API is running 🚀"}

@app.get("/books", response_model=List[BookSchema])
def get_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(Book).offset(skip).limit(limit).all()
    return books

@app.get("/books/{book_id}", response_model=BookSchema)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=BookSchema)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.put("/books/{book_id}", response_model=BookSchema)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    update_data = book.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_book, field, value)
    
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}

@app.get("/books/search", response_model=List[BookSchema])
def search_books(q: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(Book).filter(
        Book.title.ilike(f"%{q}%") | Book.author.ilike(f"%{q}%") | Book.category.ilike(f"%{q}%")
    ).offset(skip).limit(limit).all()
    return books

@app.get("/books/category/{category}", response_model=List[BookSchema])
def get_books_by_category(category: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(Book).filter(Book.category == category).offset(skip).limit(limit).all()
    return books
