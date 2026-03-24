from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, Book
import json

def seed_database():
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Check if books already exist
    existing_books = db.query(Book).first()
    if existing_books:
        print("Database already contains books. Skipping seeding.")
        return
    
    # Sample book data
    sample_books = [
        {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "description": "A classic American novel set in the Jazz Age, exploring themes of wealth, love, and the American Dream.",
            "isbn": "978-0-7432-7356-5",
            "category": "Fiction",
            "published_year": 1925,
            "cover_image_url": "https://via.placeholder.com/400x600/4F46E5/FFFFFF?text=Great+Gatsby",
            "is_available": True
        },
        {
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "description": "A powerful story of racial injustice and childhood innocence in the American South.",
            "isbn": "978-0-06-112008-4",
            "category": "Fiction",
            "published_year": 1960,
            "cover_image_url": "https://via.placeholder.com/400x600/059669/FFFFFF?text=To+Kill+a+Mockingbird",
            "is_available": True
        },
        {
            "title": "1984",
            "author": "George Orwell",
            "description": "A dystopian social science fiction novel and cautionary tale about the dangers of totalitarianism.",
            "isbn": "978-0-452-28423-4",
            "category": "Science Fiction",
            "published_year": 1949,
            "cover_image_url": "https://via.placeholder.com/400x600/DC2626/FFFFFF?text=1984",
            "is_available": True
        },
        {
            "title": "Pride and Prejudice",
            "author": "Jane Austen",
            "description": "A romantic novel of manners that charts the emotional development of the protagonist Elizabeth Bennet.",
            "isbn": "978-0-14-143951-8",
            "category": "Romance",
            "published_year": 1813,
            "cover_image_url": "https://via.placeholder.com/400x600/7C3AED/FFFFFF?text=Pride+and+Prejudice",
            "is_available": True
        },
        {
            "title": "The Catcher in the Rye",
            "author": "J.D. Salinger",
            "description": "The story of teenage rebellion and angst, narrated by the iconic Holden Caulfield.",
            "isbn": "978-0-316-76948-0",
            "category": "Fiction",
            "published_year": 1951,
            "cover_image_url": "https://via.placeholder.com/400x600/EA580C/FFFFFF?text=The+Catcher+in+the+Rye",
            "is_available": True
        },
        {
            "title": "Sapiens: A Brief History of Humankind",
            "author": "Yuval Noah Harari",
            "description": "An exploration of how Homo sapiens came to dominate the world, examining our history and future.",
            "isbn": "978-0-06-231609-7",
            "category": "Non-Fiction",
            "published_year": 2011,
            "cover_image_url": "https://via.placeholder.com/400x600/0891B2/FFFFFF?text=Sapiens",
            "is_available": True
        },
        {
            "title": "The Hobbit",
            "author": "J.R.R. Tolkien",
            "description": "A fantasy adventure about Bilbo Baggins' journey to help dwarves reclaim their mountain home from a dragon.",
            "isbn": "978-0-547-92822-7",
            "category": "Fantasy",
            "published_year": 1937,
            "cover_image_url": "https://via.placeholder.com/400x600/15803D/FFFFFF?text=The+Hobbit",
            "is_available": True
        },
        {
            "title": "Harry Potter and the Sorcerer's Stone",
            "author": "J.K. Rowling",
            "description": "The first book in the beloved series about a young wizard's magical education and adventures.",
            "isbn": "978-0-439-70818-8",
            "category": "Fantasy",
            "published_year": 1997,
            "cover_image_url": "https://via.placeholder.com/400x600/991B1B/FFFFFF?text=Harry+Potter",
            "is_available": True
        },
        {
            "title": "The Lean Startup",
            "author": "Eric Ries",
            "description": "A guide for entrepreneurs who want to build successful businesses through validated learning and rapid experimentation.",
            "isbn": "978-0-307-88789-4",
            "category": "Business",
            "published_year": 2011,
            "cover_image_url": "https://via.placeholder.com/400x600/1E40AF/FFFFFF?text=The+Lean+Startup",
            "is_available": True
        },
        {
            "title": "Atomic Habits",
            "author": "James Clear",
            "description": "A comprehensive guide to building good habits and breaking bad ones through small, incremental changes.",
            "isbn": "978-0-7352-1129-2",
            "category": "Self-Help",
            "published_year": 2018,
            "cover_image_url": "https://via.placeholder.com/400x600/713F12/FFFFFF?text=Atomic+Habits",
            "is_available": True
        }
    ]
    
    # Add books to database
    for book_data in sample_books:
        book = Book(**book_data)
        db.add(book)
    
    db.commit()
    print(f"Successfully seeded {len(sample_books)} books into the database")
    
    db.close()

if __name__ == "__main__":
    seed_database()
