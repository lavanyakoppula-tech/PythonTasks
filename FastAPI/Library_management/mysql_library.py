# ============================================================
# 📚 FastAPI Library Management System (MySQL Version)
#
# Install Packages:
# pip install fastapi uvicorn sqlalchemy pymysql
#
# Run:
# uvicorn library_mysql:app --reload
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, ConfigDict
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

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🗄️ MySQL Database Configuration
# ------------------------------------------------------------
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/library_db"

'''
mysql+pymysql://root:root@localhost:3306/library_db
│      │         │    │    │         │    │
│      │         │    │    │         │    └── Database name
│      │         │    │    │         └────── Port
│      │         │    │    └──────────────── Hostname
│      │         │    └───────────────────── Password
│      │         └────────────────────────── Username
│      └──────────────────────────────────── Driver
└─────────────────────────────────────────── Database type
'''

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine
)

Base = declarative_base()

# ------------------------------------------------------------
# 📚 Books Table
# ------------------------------------------------------------
class BookDB(Base):

    __tablename__ = "books"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(255),
        nullable=False
    )

    author = Column(
        String(255),
        nullable=False
    )

    category = Column(
        String(255),
        nullable=False
    )

    published_year = Column(
        Integer
    )

    available = Column(
        Boolean,
        default=True
    )

# ------------------------------------------------------------
# 🛠️ Create Tables
# ------------------------------------------------------------
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Book(BaseModel):

    id: int
    title: str
    author: str
    category: str
    published_year: int
    available: bool = True

    model_config = ConfigDict(
        from_attributes=True
    )

# ------------------------------------------------------------
# 🔌 Database Dependency
# ------------------------------------------------------------
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/")
def home():

    return {
        "message": "Library Management System 🚀"
    }

# ------------------------------------------------------------
# ✅ ADD NEW BOOK
# ------------------------------------------------------------
@app.post("/books")
def add_book(
    book: Book,
    db: Session = Depends(get_db)
):

    existing = db.query(BookDB).filter(
        BookDB.id == book.id
    ).first()

    if existing:

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
        "message": "Book added successfully",
        "data": new_book
    }

# ------------------------------------------------------------
# ✅ GET ALL BOOKS
# ------------------------------------------------------------
@app.get("/books")
def get_all_books(
    db: Session = Depends(get_db)
):

    books = db.query(BookDB).all()

    return {
        "count": len(books),
        "data": books
    }

# ------------------------------------------------------------
# ✅ GET BOOK BY ID
# ------------------------------------------------------------
@app.get("/books/{book_id}")
def get_book(
    book_id: int,
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

# ------------------------------------------------------------
# ✅ UPDATE BOOK
# ------------------------------------------------------------
@app.put("/books/{book_id}")
def update_book(
    book_id: int,
    updated_book: Book,
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
        "message": "Book updated successfully",
        "data": book
    }

# ------------------------------------------------------------
# ✅ DELETE BOOK
# ------------------------------------------------------------
@app.delete("/books/{book_id}")
def delete_book(
    book_id: int,
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

# ------------------------------------------------------------
# ✅ ISSUE BOOK
# ------------------------------------------------------------
@app.post("/issue-book/{book_id}")
def issue_book(
    book_id: int,
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

    if not book.available:

        raise HTTPException(
            status_code=400,
            detail="Book already issued"
        )

    book.available = False

    db.commit()

    return {
        "message": "Book issued successfully"
    }

# ------------------------------------------------------------
# ✅ RETURN BOOK
# ------------------------------------------------------------
@app.post("/return-book/{book_id}")
def return_book(
    book_id: int,
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

    if book.available:

        raise HTTPException(
            status_code=400,
            detail="Book already available"
        )

    book.available = True

    db.commit()

    return {
        "message": "Book returned successfully"
    }

# ------------------------------------------------------------
# ✅ GET AVAILABLE BOOKS
# ------------------------------------------------------------
@app.get("/available-books")
def get_available_books(
    db: Session = Depends(get_db)
):

    books = db.query(BookDB).filter(
        BookDB.available == True
    ).all()

    return {
        "count": len(books),
        "data": books
    }

# ------------------------------------------------------------
# ✅ GET ISSUED BOOKS
# ------------------------------------------------------------
@app.get("/issued-books")
def get_issued_books(
    db: Session = Depends(get_db)
):

    books = db.query(BookDB).filter(
        BookDB.available == False
    ).all()

    return {
        "count": len(books),
        "data": books
    }

# ------------------------------------------------------------
# ✅ SEARCH BOOK BY TITLE
# ------------------------------------------------------------
@app.get("/search-book/{title}")
def search_book(
    title: str,
    db: Session = Depends(get_db)
):

    books = db.query(BookDB).filter(
        BookDB.title.ilike(f"%{title}%")
    ).all()

    if not books:

        raise HTTPException(
            status_code=404,
            detail="No books found"
        )

    return {
        "count": len(books),
        "data": books
    }


