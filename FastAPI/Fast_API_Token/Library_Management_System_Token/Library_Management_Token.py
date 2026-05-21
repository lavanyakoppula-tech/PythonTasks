# ============================================================
# 🔐 FASTAPI + JWT + MYSQL LIBRARY MANAGEMENT SYSTEM
# ============================================================

# ============================================================
# ✅ INSTALL REQUIRED PACKAGES
# ============================================================

# pip install fastapi uvicorn sqlalchemy pymysql python-jose python-multipart

# ============================================================
# ✅ CREATE MYSQL DATABASE
# ============================================================

# Open MySQL and run:
#
# CREATE DATABASE jwt_library_db;

# ============================================================
# ✅ RUN APPLICATION
# ============================================================

# uvicorn main:app --reload

# ============================================================
# ✅ SWAGGER URL
# ============================================================

# http://127.0.0.1:8000/docs

# ============================================================
# 📦 IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Session
)

from jose import jwt, JWTError

from datetime import datetime, timedelta

# ============================================================
# 🚀 FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
# 🗄️ MYSQL DATABASE CONFIGURATION
# ============================================================

DB_USER = "root"

# CHANGE THIS PASSWORD
DB_PASSWORD = "root"

DB_HOST = "localhost"

DB_PORT = "3306"

DB_NAME = "jwt_library_db"

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ============================================================
# 🔌 DATABASE ENGINE
# ============================================================

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

# ============================================================
# ✅ TEST DATABASE CONNECTION
# ============================================================

try:

    connection = engine.connect()

    print("✅ MySQL Connected Successfully")

    connection.close()

except Exception as e:

    print("❌ MySQL Connection Failed")

    print(e)

# ============================================================
# 🗄️ SESSION
# ============================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ============================================================
# 🔐 JWT CONFIGURATION
# ============================================================

SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60

# ============================================================
# 🧾 PYDANTIC MODELS
# ============================================================

class User(BaseModel):

    username: str
    password: str

# ------------------------------------------------------------

class Book(BaseModel):

    id: int
    title: str
    author: str
    category: str
    published_year: int
    available: bool = True

# ============================================================
# 👤 USER TABLE
# ============================================================

class UserDB(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(100),
        unique=True
    )

    password = Column(
        String(100)
    )

# ============================================================
# 📚 BOOK TABLE
# ============================================================

class BookDB(Base):

    __tablename__ = "books"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(255),
        unique=True
    )

    author = Column(
        String(255)
    )

    category = Column(
        String(255)
    )

    published_year = Column(
        Integer
    )

    available = Column(
        Boolean,
        default=True
    )

# ============================================================
# 🛠️ CREATE TABLES
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# 🔌 DATABASE CONNECTION
# ============================================================

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()

# ============================================================
# 🔐 CREATE JWT TOKEN
# ============================================================

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# ============================================================
# 🔐 TOKEN VALIDATION
# ============================================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

# ------------------------------------------------------------

def verify_token(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token expired or invalid"
        )

# ============================================================
# 🏠 HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "FastAPI + JWT + MySQL CRUD API"
    }

# ============================================================
# 👤 REGISTER USER API
# ============================================================

@app.post("/register")
def register(
    user: User,
    db: Session = Depends(get_db)
):

    existing_user = db.query(UserDB).filter(
        UserDB.username == user.username
    ).first()

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = UserDB(
        username=user.username,
        password=user.password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }

# ============================================================
# 🔐 LOGIN API
# ============================================================

@app.post("/login")
def login(
    user: User,
    db: Session = Depends(get_db)
):

    existing_user = db.query(UserDB).filter(
        UserDB.username == user.username
    ).first()

    if not existing_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid username"
        )

    if existing_user.password != user.password:

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "message": "Login successful",
        "access_token": access_token,
        "token_type": "bearer"
    }

# ============================================================
# ➕ CREATE BOOK API
# ============================================================

@app.post("/books")
def create_book(
    book: Book,
    user: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    existing_book = db.query(BookDB).filter(
        BookDB.id == book.id
    ).first()

    if existing_book:

        raise HTTPException(
            status_code=400,
            detail="Book ID already exists"
        )

    new_book = BookDB(
        id=book.id,
        title=book.title,
        author=book.author,
        category=book.category,
        published_year=book.published_year,
        available=book.available
    )

    db.add(new_book)

    db.commit()

    db.refresh(new_book)

    return {
        "message": "Book created successfully",
        "data": {
            "id": new_book.id,
            "title": new_book.title,
            "author": new_book.author,
            "category": new_book.category,
            "published_year": new_book.published_year,
            "available": new_book.available
        }
    }

# ============================================================
# 📚 GET ALL BOOKS API
# ============================================================

@app.get("/books")
def get_books(
    user: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    books = db.query(BookDB).all()

    return books

# ============================================================
# 📖 GET SINGLE BOOK API
# ============================================================

@app.get("/books/{book_id}")
def get_book(
    book_id: int,
    user: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    book = db.query(BookDB).filter(
        BookDB.id == book_id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book

# ============================================================
# ✏️ UPDATE BOOK API
# ============================================================

@app.put("/books/{book_id}")
def update_book(
    book_id: int,
    updated_book: Book,
    user: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    book = db.query(BookDB).filter(
        BookDB.id == book_id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    book.title = updated_book.title
    book.author = updated_book.author
    book.category = updated_book.category
    book.published_year = updated_book.published_year
    book.available = updated_book.available

    db.commit()

    db.refresh(book)

    return {
        "message": "Book updated successfully"
    }

# ============================================================
# ❌ DELETE BOOK API
# ============================================================

@app.delete("/books/{book_id}")
def delete_book(
    book_id: int,
    user: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    book = db.query(BookDB).filter(
        BookDB.id == book_id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    db.delete(book)

    db.commit()

    return {
        "message": "Book deleted successfully"
    }

# ============================================================
# ✅ POSTMAN TESTING
# ============================================================

# 1. REGISTER USER
#
# POST
# http://127.0.0.1:8000/register
#
# BODY -> RAW -> JSON
#
# {
#     "username": "admin",
#     "password": "admin123"
# }

# ============================================================

# 2. LOGIN USER
#
# POST
# http://127.0.0.1:8000/login
#
# BODY -> RAW -> JSON
#
# {
#     "username": "admin",
#     "password": "admin123"
# }

# ============================================================

# LOGIN RESPONSE
#
# {
#   "message": "Login successful",
#   "access_token": "eyJhbGciOi...",
#   "token_type": "bearer"
# }

# ============================================================

# 3. COPY TOKEN
#
# COPY access_token VALUE

# ============================================================

# 4. CREATE BOOK
#
# POST
# http://127.0.0.1:8000/books
#
# HEADERS
#
# Authorization : Bearer YOUR_TOKEN
#
# BODY -> RAW -> JSON
#
# {
#     "id": 1,
#     "title": "Python",
#     "author": "Sai",
#     "category": "Programming",
#     "published_year": 2025,
#     "available": true
# }

# ============================================================

# 5. GET ALL BOOKS
#
# GET
# http://127.0.0.1:8000/books
#
# HEADERS
#
# Authorization : Bearer YOUR_TOKEN

# ============================================================
