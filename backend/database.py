import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables from a local .env if present.
load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://pramod:Pramod%4013091876@localhost/digital_library",
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
