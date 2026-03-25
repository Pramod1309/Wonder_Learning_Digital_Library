import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Admin
from schemas import AdminLoginRequest, AdminLoginResponse
from passlib.context import CryptContext

app = FastAPI(title="Wonder Learning Digital Library API")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "pramod.wonderlearning@gmail.com")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "Pramod@1309")

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

@app.post("/admin/login", response_model=AdminLoginResponse)
def admin_login(payload: AdminLoginRequest, db: Session = Depends(get_db)):
    try:
        Admin.__table__.create(bind=engine, checkfirst=True)
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Unable to initialize admin table. {exc}",
        )

    if payload.email.strip().lower() != ADMIN_EMAIL.strip().lower():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    admin = db.query(Admin).filter(Admin.email == ADMIN_EMAIL).first()

    if admin is None:
        if payload.password != ADMIN_PASSWORD:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        admin = Admin(
            email=ADMIN_EMAIL,
            hashed_password=pwd_context.hash(ADMIN_PASSWORD),
        )
        db.add(admin)
        db.commit()
        db.refresh(admin)
    else:
        if not pwd_context.verify(payload.password, admin.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    return AdminLoginResponse(
        access_token="admin-token",
        token_type="bearer",
        user_type="admin",
        email=admin.email,
    )

