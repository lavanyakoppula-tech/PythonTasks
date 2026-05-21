# ============================================================
# 📚 REAL-WORLD LIBRARY MANAGEMENT SYSTEM
# 📚 FASTAPI + MONGODB ATLAS + MONGOENGINE
# ============================================================

# ============================================================
# 🚀 INSTALL PACKAGES
# ============================================================

'''
pip install fastapi uvicorn mongoengine pymongo
'''

# ============================================================
# 📦 IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from mongoengine import (
    connect,
    Document,
    IntField,
    StringField,
    BooleanField,
    DateField
)

from datetime import date, timedelta

# ============================================================
# 🚀 FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
# 🌐 MONGODB ATLAS CONNECTION
# ============================================================

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

# ============================================================
# 👤 USERS COLLECTION
# ============================================================

class UserDB(Document):

    id = IntField(
        primary_key=True
    )

    student_name = StringField(
        required=True
    )

    email = StringField(
        required=True,
        unique=True
    )

    department = StringField(
        required=True
    )

    meta = {
        "collection": "users"
    }

# ============================================================
# 👨‍🏫 LIBRARIANS COLLECTION
# ============================================================

class LibrarianDB(Document):

    id = IntField(
        primary_key=True
    )

    librarian_name = StringField(
        required=True
    )

    employee_id = StringField(
        required=True,
        unique=True
    )

    meta = {
        "collection": "librarians"
    }

# ============================================================
# 📚 BOOKS COLLECTION
# ============================================================

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

    edition = StringField(
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

# ============================================================
# 📘 ISSUED BOOKS COLLECTION
# ============================================================

class IssuedBookDB(Document):

    issue_id = IntField(
        primary_key=True
    )

    book_id = IntField(
        required=True
    )

    user_id = IntField(
        required=True
    )

    librarian_id = IntField(
        required=True
    )

    issued_date = DateField(
        required=True
    )

    return_deadline = DateField(
        required=True
    )

    returned_date = DateField()

    issue_status = BooleanField(
        default=True
    )

    meta = {
        "collection": "issued_books"
    }

# ============================================================
# 🧾 PYDANTIC MODELS
# ============================================================

class User(BaseModel):

    id: int
    student_name: str
    email: str
    department: str

# ------------------------------------------------------------

class Librarian(BaseModel):

    id: int
    librarian_name: str
    employee_id: str

# ------------------------------------------------------------

class Book(BaseModel):

    id: int
    title: str
    author: str
    category: str
    edition: str
    published_year: int
    available: bool = True

# ------------------------------------------------------------

class IssueBook(BaseModel):

    issue_id: int
    book_id: int
    user_id: int
    librarian_id: int
    days: int

# ============================================================
# 🏠 HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Real-World MongoDB Library System 🚀"
    }

# ============================================================
# ✅ ADD USER
# ============================================================

@app.post("/users")
def add_user(user: User):

    try:

        existing = UserDB.objects(
            id=user.id
        ).first()

        if existing:

            raise HTTPException(
                status_code=400,
                detail="User already exists"
            )

        new_user = UserDB(
            id=user.id,
            student_name=user.student_name,
            email=user.email,
            department=user.department
        )

        new_user.save()

        return {
            "message": "User added successfully"
        }

    except HTTPException as e:

        raise e

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to add user"
        )

# ============================================================
# ✅ ADD LIBRARIAN
# ============================================================

@app.post("/librarians")
def add_librarian(librarian: Librarian):

    try:

        existing = LibrarianDB.objects(
            id=librarian.id
        ).first()

        if existing:

            raise HTTPException(
                status_code=400,
                detail="Librarian already exists"
            )

        new_librarian = LibrarianDB(
            id=librarian.id,
            librarian_name=librarian.librarian_name,
            employee_id=librarian.employee_id
        )

        new_librarian.save()

        return {
            "message": "Librarian added successfully"
        }

    except HTTPException as e:

        raise e

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to add librarian"
        )

# ============================================================
# ✅ ADD BOOK
# ============================================================

@app.post("/books")
def add_book(book: Book):

    try:

        existing = BookDB.objects(
            id=book.id
        ).first()

        if existing:

            raise HTTPException(
                status_code=400,
                detail="Book already exists"
            )

        new_book = BookDB(
            id=book.id,
            title=book.title,
            author=book.author,
            category=book.category,
            edition=book.edition,
            published_year=book.published_year,
            available=True
        )

        new_book.save()

        return {
            "message": "Book added successfully"
        }

    except HTTPException as e:

        raise e

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to add book"
        )

# ============================================================
# ✅ GET ALL BOOKS
# ============================================================

@app.get("/books")
def get_books():

    try:

        books = BookDB.objects()

        data = []

        for book in books:

            data.append({
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "category": book.category,
                "edition": book.edition,
                "published_year": book.published_year,
                "available": book.available
            })

        return {
            "count": len(data),
            "data": data
        }

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to fetch books"
        )

# ============================================================
# ✅ ISSUE BOOK
# ============================================================

@app.post("/issue-book")
def issue_book(issue: IssueBook):

    try:

        # Check Book
        book = BookDB.objects(
            id=issue.book_id
        ).first()

        if not book:

            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        # Check Availability
        if not book.available:

            raise HTTPException(
                status_code=400,
                detail="Book already issued"
            )

        # Check User
        user = UserDB.objects(
            id=issue.user_id
        ).first()

        if not user:

            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        # Check Librarian
        librarian = LibrarianDB.objects(
            id=issue.librarian_id
        ).first()

        if not librarian:

            raise HTTPException(
                status_code=404,
                detail="Librarian not found"
            )

        # Dates
        issued_date = date.today()

        return_deadline = issued_date + timedelta(
            days=issue.days
        )

        # Create Issue Record
        issue_record = IssuedBookDB(
            issue_id=issue.issue_id,
            book_id=issue.book_id,
            user_id=issue.user_id,
            librarian_id=issue.librarian_id,
            issued_date=issued_date,
            return_deadline=return_deadline,
            issue_status=True
        )

        issue_record.save()

        # Update Book Availability
        book.available = False

        book.save()

        return {
            "message": "Book issued successfully",
            "issued_to": user.student_name,
            "issued_by": librarian.librarian_name,
            "deadline": return_deadline
        }

    except HTTPException as e:

        raise e

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to issue book"
        )

# ============================================================
# ✅ RETURN BOOK
# ============================================================

@app.post("/return-book/{book_id}")
def return_book(book_id: int):

    try:

        issue_record = IssuedBookDB.objects(
            book_id=book_id,
            issue_status=True
        ).first()

        if not issue_record:

            raise HTTPException(
                status_code=404,
                detail="Issued record not found"
            )

        book = BookDB.objects(
            id=book_id
        ).first()

        issue_record.issue_status = False

        issue_record.returned_date = date.today()

        issue_record.save()

        # Update availability
        book.available = True

        book.save()

        return {
            "message": "Book returned successfully"
        }

    except HTTPException as e:

        raise e

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to return book"
        )

# ============================================================
# ✅ GET AVAILABLE BOOKS
# ============================================================

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
            "available": book.available
        })

    return {
        "count": len(data),
        "data": data
    }

# ============================================================
# ✅ GET ISSUED BOOKS HISTORY
# ============================================================

@app.get("/issued-books")
def issued_books():

    books = IssuedBookDB.objects()

    data = []

    for book in books:

        data.append({
            "issue_id": book.issue_id,
            "book_id": book.book_id,
            "user_id": book.user_id,
            "librarian_id": book.librarian_id,
            "issued_date": book.issued_date,
            "deadline": book.return_deadline,
            "returned_date": book.returned_date,
            "issue_status": book.issue_status
        })

    return {
        "count": len(data),
        "data": data
    }
