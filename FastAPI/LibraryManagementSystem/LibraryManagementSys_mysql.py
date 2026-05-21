# ============================================================
# 📚 REAL-WORLD LIBRARY MANAGEMENT SYSTEM
# 📚 FASTAPI + MYSQL + REAL-TIME TABLE MAPPING
# ============================================================

# ============================================================
# 🚀 INSTALL PACKAGES
# ============================================================

'''
pip install fastapi uvicorn sqlalchemy pymysql
'''

# ============================================================
# 📦 IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends

from pydantic import BaseModel, ConfigDict

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    Date,
    ForeignKey
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    Session
)

from datetime import date, timedelta

# ============================================================
# 🚀 FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
# 🗄️ MYSQL DATABASE CONNECTION
# ============================================================

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/library_db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ============================================================
# 👤 USERS TABLE
# ============================================================

class UserDB(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    student_name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False
    )

    department = Column(
        String(100),
        nullable=False
    )

# ============================================================
# 👨‍🏫 LIBRARIANS TABLE
# ============================================================

class LibrarianDB(Base):

    __tablename__ = "librarians"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    librarian_name = Column(
        String(100),
        nullable=False
    )

    employee_id = Column(
        String(100),
        unique=True,
        nullable=False
    )

# ============================================================
# 📚 BOOKS TABLE
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

    edition = Column(
        String(100),
        nullable=False
    )

    published_year = Column(
        Integer,
        nullable=False
    )

    available = Column(
        Boolean,
        default=True
    )

# ============================================================
# 📘 ISSUED BOOKS TABLE
# ============================================================

class IssuedBookDB(Base):

    __tablename__ = "issued_books"

    issue_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    book_id = Column(
        Integer,
        ForeignKey("books.id")
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    librarian_id = Column(
        Integer,
        ForeignKey("librarians.id")
    )

    issued_date = Column(
        Date,
        nullable=False
    )

    return_deadline = Column(
        Date,
        nullable=False
    )

    returned_date = Column(
        Date,
        nullable=True
    )

    issue_status = Column(
        Boolean,
        default=True
    )

# ============================================================
# 🛠️ CREATE TABLES
# ============================================================

Base.metadata.create_all(bind=engine)

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

    model_config = ConfigDict(
        from_attributes=True
    )

# ------------------------------------------------------------

class IssueBook(BaseModel):

    book_id: int
    user_id: int
    librarian_id: int
    days: int

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
# 🏠 HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Real Library Management System 🚀"
    }

# ============================================================
# ✅ ADD USER
# ============================================================

@app.post("/users")
def add_user(
    user: User,
    db: Session = Depends(get_db)
):

    try:

        existing_user = db.query(UserDB).filter(
            UserDB.id == user.id
        ).first()

        if existing_user:

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

        db.add(new_user)

        db.commit()

        return {
            "message": "User added successfully"
        }

    except HTTPException as e:

        raise e

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Unable to add user"
        )

# ============================================================
# ✅ ADD LIBRARIAN
# ============================================================

@app.post("/librarians")
def add_librarian(
    librarian: Librarian,
    db: Session = Depends(get_db)
):

    try:

        existing_librarian = db.query(
            LibrarianDB
        ).filter(
            LibrarianDB.id == librarian.id
        ).first()

        if existing_librarian:

            raise HTTPException(
                status_code=400,
                detail="Librarian already exists"
            )

        new_librarian = LibrarianDB(
            id=librarian.id,
            librarian_name=librarian.librarian_name,
            employee_id=librarian.employee_id
        )

        db.add(new_librarian)

        db.commit()

        return {
            "message": "Librarian added successfully"
        }

    except HTTPException as e:

        raise e

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Unable to add librarian"
        )

# ============================================================
# ✅ ADD BOOK
# ============================================================

@app.post("/books")
def add_book(
    book: Book,
    db: Session = Depends(get_db)
):

    try:

        existing_book = db.query(BookDB).filter(
            BookDB.id == book.id
        ).first()

        if existing_book:

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

        db.add(new_book)

        db.commit()

        return {
            "message": "Book added successfully"
        }

    except HTTPException as e:

        raise e

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Unable to add book"
        )

# ============================================================
# ✅ GET ALL BOOKS
# ============================================================

@app.get("/books")
def get_books(
    db: Session = Depends(get_db)
):

    try:

        books = db.query(BookDB).all()

        return {
            "count": len(books),
            "data": books
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
def issue_book(
    issue: IssueBook,
    db: Session = Depends(get_db)
):

    try:

        # Check Book
        book = db.query(BookDB).filter(
            BookDB.id == issue.book_id
        ).first()

        if not book:

            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        # Check Availability
        if book.available == False:

            raise HTTPException(
                status_code=400,
                detail="Book already issued"
            )

        # Check User
        user = db.query(UserDB).filter(
            UserDB.id == issue.user_id
        ).first()

        if not user:

            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        # Check Librarian
        librarian = db.query(LibrarianDB).filter(
            LibrarianDB.id == issue.librarian_id
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

        # Issue Record
        issue_record = IssuedBookDB(
            book_id=issue.book_id,
            user_id=issue.user_id,
            librarian_id=issue.librarian_id,
            issued_date=issued_date,
            return_deadline=return_deadline,
            issue_status=True
        )

        db.add(issue_record)

        # Update Availability
        book.available = False

        db.commit()

        return {
            "message": "Book issued successfully",
            "issued_to": user.student_name,
            "issued_by": librarian.librarian_name,
            "deadline": return_deadline
        }

    except HTTPException as e:

        raise e

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Unable to issue book"
        )

# ============================================================
# ✅ RETURN BOOK
# ============================================================

@app.post("/return-book/{book_id}")
def return_book(
    book_id: int,
    db: Session = Depends(get_db)
):

    try:

        issue_record = db.query(
            IssuedBookDB
        ).filter(
            IssuedBookDB.book_id == book_id,
            IssuedBookDB.issue_status == True
        ).first()

        if not issue_record:

            raise HTTPException(
                status_code=404,
                detail="Issued record not found"
            )

        book = db.query(BookDB).filter(
            BookDB.id == book_id
        ).first()

        issue_record.issue_status = False

        issue_record.returned_date = date.today()

        book.available = True

        db.commit()

        return {
            "message": "Book returned successfully"
        }

    except HTTPException as e:

        raise e

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Unable to return book"
        )

# ============================================================
# ✅ GET AVAILABLE BOOKS
# ============================================================

@app.get("/available-books")
def available_books(
    db: Session = Depends(get_db)
):

    try:

        books = db.query(BookDB).filter(
            BookDB.available == True
        ).all()

        return {
            "count": len(books),
            "data": books
        }

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to fetch available books"
        )

# ============================================================
# ✅ GET ISSUED BOOKS HISTORY
# ============================================================

@app.get("/issued-books")
def issued_books(
    db: Session = Depends(get_db)
):

    try:

        books = db.query(
            IssuedBookDB
        ).all()

        return {
            "count": len(books),
            "data": books
        }

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to fetch issued books"
        )

# ============================================================
# 🌐 RUN SERVER
# ============================================================

'''
uvicorn main:app --reload
'''

# ============================================================
# 🌐 SWAGGER URL
# ============================================================

'''
http://127.0.0.1:8000/docs
'''
