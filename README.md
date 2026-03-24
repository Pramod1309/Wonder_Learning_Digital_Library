# Wonder Learning Digital Library

A full-stack digital library application built with React (frontend) and FastAPI (backend) with PostgreSQL database.

## Features

- 📚 Browse and search books
- 🔍 Search by title, author, or category
- 📂 Filter books by category
- 📖 View book details and availability
- 🎨 Modern, responsive UI with Tailwind CSS
- 🚀 Fast API backend with full CRUD operations
- 🗄️ PostgreSQL database with SQLAlchemy ORM

## Tech Stack

### Frontend
- React 19
- Vite
- Tailwind CSS
- Axios for API calls

### Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic for data validation

## Prerequisites

- Node.js (v18 or higher)
- Python 3.8+
- PostgreSQL
- Git

## Setup Instructions

### 1. Database Setup

Make sure PostgreSQL is installed and running. Update the database URL in `backend/database.py`:

```python
DATABASE_URL = "postgresql://username:password@localhost/digital_library"
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Seed the database with sample data
python seed_data.py

# Start the backend server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend API will be available at: http://localhost:8000

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start the frontend development server
npm run dev
```

The frontend will be available at: http://localhost:5173

## API Endpoints

### Books
- `GET /books` - Get all books
- `GET /books/{book_id}` - Get a specific book
- `POST /books` - Create a new book
- `PUT /books/{book_id}` - Update a book
- `DELETE /books/{book_id}` - Delete a book
- `GET /books/search?q=query` - Search books
- `GET /books/category/{category}` - Get books by category

### Health Check
- `GET /` - API health check

## Project Structure

```
Wonder Learning Digital Library/
├── backend/
│   ├── main.py           # FastAPI application
│   ├── database.py       # Database connection
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic schemas
│   ├── seed_data.py      # Database seeding script
│   └── requirements.txt  # Python dependencies
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── BookList.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   └── App.jsx
│   ├── package.json
│   └── ...
└── README.md
```

## Usage

1. Start both the backend and frontend servers
2. Open http://localhost:5173 in your browser
3. Browse the digital library, search for books, or filter by category

## Development

### Adding New Books

You can add books through the API:

```bash
curl -X POST "http://localhost:8000/books" \
-H "Content-Type: application/json" \
-d '{
  "title": "New Book",
  "author": "Author Name",
  "description": "Book description",
  "category": "Fiction",
  "published_year": 2023
}'
```

### API Documentation

Once the backend is running, visit:
- http://localhost:8000/docs - Interactive API documentation (Swagger UI)
- http://localhost:8000/redoc - ReDoc documentation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.