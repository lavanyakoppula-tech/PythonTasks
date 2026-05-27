# ============================================================
# 📚 REAL-WORLD LIBRARY MANAGEMENT SYSTEM
# 📚 FASTAPI + MYSQL + SQLALCHEMY
# 📚 COMPLETE CRUD + ISSUE + RETURN + HISTORY
# ============================================================

# ============================================================
# 🚀 INSTALL REQUIRED PACKAGES
# ============================================================

'''
pip install fastapi uvicorn sqlalchemy pymysql
'''

# ============================================================
# 📦 IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends

from pydantic import BaseModel

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

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/LibManagSys_db"

engine = create_engine(
    DATABASE_URL
)

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

    phone = Column(
        String(20),
        unique=True,
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

    shift_time = Column(
        String(50)
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

    Book_uniqueid = Column(
        String(100),
        unique=True,
        nullable=False
    )

    published_year = Column(
        Integer,
        nullable=False
    )

    rack_number = Column(
        String(50)
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

    fine_amount = Column(
        Integer,
        default=0
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
    phone: str

# ------------------------------------------------------------

class Librarian(BaseModel):

    id: int
    librarian_name: str
    employee_id: str
    shift_time: str

# ------------------------------------------------------------

class Book(BaseModel):

    id: int
    title: str
    author: str
    category: str
    edition: str
    Book_uniqueid: str
    published_year: int
    rack_number: str
    available: bool = True
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
        "message": "Real-World Library Management System 🚀"
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
            UserDB.email == user.email
        ).first()

        if existing_user:

            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        new_user = UserDB(
            id=user.id,
            student_name=user.student_name,
            email=user.email,
            department=user.department,
            phone=user.phone
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
# ✅ GET USERS
# ============================================================

@app.get("/users")
def get_users(
    db: Session = Depends(get_db)
):

    users = db.query(UserDB).all()

    return {
        "count": len(users),
        "data": users
    }

# ============================================================
# ✅ ADD LIBRARIAN
# ============================================================

@app.post("/librarians")
def add_librarian(
    librarian: Librarian,
    db: Session = Depends(get_db)
):

    try:

        existing = db.query(
            LibrarianDB
        ).filter(
            LibrarianDB.employee_id == librarian.employee_id
        ).first()

        if existing:

            raise HTTPException(
                status_code=400,
                detail="Employee ID already exists"
            )

        new_librarian = LibrarianDB(
            id=librarian.id,
            librarian_name=librarian.librarian_name,
            employee_id=librarian.employee_id,
            shift_time=librarian.shift_time
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
# ✅ GET LIBRARIANS
# ============================================================

@app.get("/librarians")
def get_librarians(
    db: Session = Depends(get_db)
):

    librarians = db.query(
        LibrarianDB
    ).all()

    return {
        "count": len(librarians),
        "data": librarians
    }

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
            BookDB.Book_uniqueid == book.Book_uniqueid
        ).first()

        if existing_book:

            raise HTTPException(
                status_code=400,
                detail="ISBN already exists"
            )

        new_book = BookDB(
            id=book.id,
            title=book.title,
            author=book.author,
            category=book.category,
            edition=book.edition,
            Book_uniqueid=book.Book_uniqueid,
            published_year=book.published_year,
            rack_number=book.rack_number,
            available = Column(Boolean, default=True)
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

    books = db.query(BookDB).all()

    return {
        "count": len(books),
        "data": books
    }

# ============================================================
# ✅ GET BOOK BY ID
# ============================================================

@app.get("/books/{book_id}")
def get_book_by_id(
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

# ============================================================
# ✅ UPDATE BOOK
# ============================================================

@app.put("/books/{book_id}")
def update_book(
    book_id: int,
    updated_book: Book,
    db: Session = Depends(get_db)
):

    try:

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
        book.edition = updated_book.edition
        book.published_year = updated_book.published_year
        book.rack_number = updated_book.rack_number

        db.commit()

        return {
            "message": "Book updated successfully"
        }

    except HTTPException as e:

        raise e

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Unable to update book"
        )

# ============================================================
# ✅ DELETE BOOK
# ============================================================

@app.delete("/books/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):

    try:

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

    except HTTPException as e:

        raise e

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Unable to delete book"
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

        # CHECK BOOK
        book = db.query(BookDB).filter(
            BookDB.id == issue.book_id
        ).first()

        if not book:

            raise HTTPException(
                status_code=404,
                detail="Book not found"
            )

        # CHECK AVAILABILITY
        if book.available == False:

            raise HTTPException(
                status_code=400,
                detail="Book already issued"
            )

        # CHECK USER
        user = db.query(UserDB).filter(
            UserDB.id == issue.user_id
        ).first()

        if not user:

            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        # CHECK LIBRARIAN
        librarian = db.query(
            LibrarianDB
        ).filter(
            LibrarianDB.id == issue.librarian_id
        ).first()

        if not librarian:

            raise HTTPException(
                status_code=404,
                detail="Librarian not found"
            )

        # ISSUE DATES
        issued_date = date.today()

        return_deadline = issued_date + timedelta(
            days=issue.days
        )

        # CREATE ISSUE RECORD
        issue_record = IssuedBookDB(
            book_id=issue.book_id,
            user_id=issue.user_id,
            librarian_id=issue.librarian_id,
            issued_date=issued_date,
            return_deadline=return_deadline,
            issue_status=True
        )

        db.add(issue_record)

        # UPDATE AVAILABILITY
        book.available = False

        db.commit()

        return {
            "message": "Book issued successfully",
            "issued_date": issued_date,
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

        # UPDATE ISSUE RECORD
        issue_record.issue_status = False

        issue_record.returned_date = date.today()

        # UPDATE BOOK STATUS
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
# ✅ AVAILABLE BOOKS
# ============================================================

@app.get("/available-books")
def available_books(
    db: Session = Depends(get_db)
):

    books = db.query(BookDB).filter(
        BookDB.available == True
    ).all()

    return {
        "count": len(books),
        "data": books
    }

# ============================================================
# ✅ ISSUED BOOKS HISTORY
# ============================================================

@app.get("/issued-books")
def issued_books(
    db: Session = Depends(get_db)
):

    books = db.query(
        IssuedBookDB
    ).all()

    return {
        "count": len(books),
        "data": books
    }

