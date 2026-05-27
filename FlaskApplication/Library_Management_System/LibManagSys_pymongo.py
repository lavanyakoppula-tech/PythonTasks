# ============================================================
# 📚 FastAPI Library Management System (MongoDB Version)
#
# Install Packages:
# pip install fastapi uvicorn mongoengine pymongo
#
# Run:
# uvicorn mongo_library:app --reload
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import (
    connect,
    Document,
    IntField,
    StringField,
    BooleanField
)

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------
MONGO_URL = "mongodb+srv://lavanya_db_user:d2EpVuZm2mFknSTN@lavanya.7ovtsto.mongodb.net/library_db?retryWrites=true&w=majority"

try:

    connect(
        db="library_db",
        host=MONGO_URL
    )

    print("✅ MongoDB Atlas Connected Successfully")

except Exception as e:

    print("❌ MongoDB Connection Failed")
    print(e)

# ------------------------------------------------------------
# 📚 MongoDB Book Model
# ------------------------------------------------------------
class BookDB(Document):

    id = IntField(
        primary_key=True
    )

    title = StringField(
        required=True
    )

    author = StringField(
        required=True
    )

    category = StringField(
        required=True
    )

    published_year = IntField(
        required=True
    )

    available = BooleanField(
        default=True
    )

    meta = {
        "collection": "books"
    }

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

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/")
def home():

    return {
        "message": "Library Management System with MongoDB 🚀"
    }

# ------------------------------------------------------------
# ✅ ADD NEW BOOK
# ------------------------------------------------------------
@app.post("/books")
def add_book(book: Book):

    existing = BookDB.objects(
        id=book.id
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

    new_book.save()

    return {
        "message": "Book added successfully",
        "data": {
            "id": new_book.id,
            "title": new_book.title,
            "author": new_book.author,
            "category": new_book.category,
            "published_year": new_book.published_year,
            "available": new_book.available
        }
    }

# ------------------------------------------------------------
# ✅ GET ALL BOOKS
# ------------------------------------------------------------
@app.get("/books")
def get_all_books():

    books = BookDB.objects()

    data = []

    for book in books:

        data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "published_year": book.published_year,
            "available": book.available
        })

    return {
        "count": len(data),
        "data": data
    }

# ------------------------------------------------------------
# ✅ GET BOOK BY ID
# ------------------------------------------------------------
@app.get("/books/{book_id}")
def get_book(book_id: int):

    book = BookDB.objects(
        id=book_id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "category": book.category,
        "published_year": book.published_year,
        "available": book.available
    }

# ------------------------------------------------------------
# ✅ UPDATE BOOK
# ------------------------------------------------------------
@app.put("/books/{book_id}")
def update_book(
    book_id: int,
    updated_book: Book
):

    book = BookDB.objects(
        id=book_id
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

    book.save()

    return {
        "message": "Book updated successfully"
    }

# ------------------------------------------------------------
# ✅ DELETE BOOK
# ------------------------------------------------------------
@app.delete("/books/{book_id}")
def delete_book(book_id: int):

    book = BookDB.objects(
        id=book_id
    ).first()

    if not book:

        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    book.delete()

    return {
        "message": "Book deleted successfully"
    }

# ------------------------------------------------------------
# ✅ ISSUE BOOK
# ------------------------------------------------------------
@app.post("/issue-book/{book_id}")
def issue_book(book_id: int):

    book = BookDB.objects(
        id=book_id
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

    book.save()

    return {
        "message": "Book issued successfully"
    }

# ------------------------------------------------------------
# ✅ RETURN BOOK
# ------------------------------------------------------------
@app.post("/return-book/{book_id}")
def return_book(book_id: int):

    book = BookDB.objects(
        id=book_id
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

    book.save()

    return {
        "message": "Book returned successfully"
    }

# ------------------------------------------------------------
# ✅ GET AVAILABLE BOOKS
# ------------------------------------------------------------
@app.get("/available-books")
def available_books():

    books = BookDB.objects(
        available=True
    )

    data = []

    for book in books:

        data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "published_year": book.published_year,
            "available": book.available
        })

    return {
        "count": len(data),
        "data": data
    }

# ------------------------------------------------------------
# ✅ GET ISSUED BOOKS
# ------------------------------------------------------------
@app.get("/issued-books")
def issued_books():

    books = BookDB.objects(
        available=False
    )

    data = []

    for book in books:

        data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "published_year": book.published_year,
            "available": book.available
        })

    return {
        "count": len(data),
        "data": data
    }

# ------------------------------------------------------------
# ✅ SEARCH BOOK BY TITLE
# ------------------------------------------------------------
@app.get("/search-book/{title}")
def search_book(title: str):

    books = BookDB.objects(
        title__icontains=title
    )

    data = []

    for book in books:

        data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "published_year": book.published_year,
            "available": book.available
        })

    if len(data) == 0:

        raise HTTPException(
            status_code=404,
            detail="No books found"
        )

    return {
        "count": len(data),
        "data": data
    }

