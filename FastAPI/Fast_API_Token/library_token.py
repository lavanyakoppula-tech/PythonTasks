# ============================================================
# 🔐 FastAPI Library Management System + JWT Authentication
# 🔐 MySQL + Exception Handling Version
# ============================================================

# ============================================================
# 🚀 WHAT WE ARE BUILDING
# ============================================================

'''
This project includes:

✅ FastAPI
✅ MySQL Database
✅ JWT Authentication
✅ CRUD Operations
✅ Protected APIs using Token
✅ Exception Handling
✅ Duplicate Validation
✅ Production Level APIs

Database used:
MySQL
'''

# ============================================================
# 🚀 INSTALL REQUIRED PACKAGES
# ============================================================

'''
pip install fastapi uvicorn sqlalchemy pymysql
pip install python-jose
pip install python-multipart
'''

# ============================================================
# 📦 IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import declarative_base
from fastapi.security import OAuth2PasswordBearer
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

from sqlalchemy.exc import SQLAlchemyError

from jose import JWTError, jwt

from datetime import datetime, timedelta

# ============================================================
# 🚀 CREATE FASTAPI APP
# ============================================================

app = FastAPI()
#==========================
# 🔐 JWT CONFIGURATION
# ============================================================

'''
SECRET_KEY
-----------
Used to sign the token
'''

SECRET_KEY = "mysecretkey"

# ------------------------------------------------------------

'''
ALGORITHM
-----------
Encryption algorithm used to create token

HS256 = Most commonly used JWT algorithm
'''

ALGORITHM = "HS256"

# ------------------------------------------------------------

'''
TOKEN EXPIRY TIME
------------------

1 Hour Token Expiry
'''

ACCESS_TOKEN_EXPIRE = timedelta(hours=1)

# ============================================================
# 🧾 PYDANTIC MODELS
# ============================================================

'''
Used for:
- Request validation
- Data structure
- Auto API documentation
'''

class Login(BaseModel):

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

    model_config = ConfigDict(
        from_attributes=True
    )

# ============================================================
# 👤 MYSQL USER TABLE
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

    email = Column(
        String(150),
        unique=True
    )

    password = Column(
        String(100)
    )

# ============================================================
# 📚 MYSQL BOOK TABLE
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
        unique=True,
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
        Integer,
        nullable=False
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

    '''
    Steps:
    1. Copy incoming data
    2. Add expiry time
    3. Encode token using secret key
    4. Return generated JWT token
    '''

    try:

        # Copy data
        to_encode = data.copy()

        # Create expiry time
        expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE

        '''
        Example:

        Current Time = 10:00 AM

        Expiry = 1 Hour

        Token Expiry = 11:00 AM
        '''

        # Add expiry into payload
        to_encode.update({"exp": expire})

        '''
        Final JWT Payload Example:

        {
            "sub": "admin",
            "exp": "11:00 AM"
        }
        '''

        # Generate encoded JWT token
        encoded_jwt = jwt.encode(
            to_encode,
            SECRET_KEY,
            algorithm=ALGORITHM
        )

        return encoded_jwt

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to create access token"
        )

# ============================================================
# 🔐 TOKEN VALIDATION
# ============================================================

'''
OAuth2PasswordBearer
---------------------

Automatically:
- Reads Authorization header
- Extracts Bearer token

Example Header:

Authorization: Bearer eyJhbGc...
'''

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)

# ------------------------------------------------------------

def verify_token(
    token: str = Depends(oauth2_scheme)
):

    '''
    This function validates token.

    Steps:
    1. Read token
    2. Decode token
    3. Verify secret key
    4. Verify expiry time
    5. Extract user info
    '''

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        '''
        Example Payload:

        {
            "sub": "admin",
            "exp": "11:00 AM"
        }
        '''

        # Extract username
        username = payload.get("sub")

        # Check username exists
        if username is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:

        '''
        Happens when:
        - Token expired
        - Wrong secret key
        - Invalid token
        '''

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
        "message": "FastAPI + JWT + MySQL CRUD 🚀"
    }

# ============================================================
# 🔐 LOGIN API
# ============================================================

@app.post("/login")
def login(
    user: Login,
    db: Session = Depends(get_db)
):

    '''
    Login Flow:

    1. Check user exists in MySQL
    2. Verify password
    3. Generate JWT token
    4. Return token
    '''

    try:

        existing_user = db.query(UserDB).filter(
            UserDB.username == user.username
        ).first()

        # Username validation
        if not existing_user:

            raise HTTPException(
                status_code=401,
                detail="Invalid username"
            )

        # Password validation
        if existing_user.password != user.password:

            raise HTTPException(
                status_code=401,
                detail="Invalid password"
            )

        '''
        Create token with username

        "sub" = subject/user
        '''

        access_token = create_access_token(
            data={"sub": user.username}
        )

        return {
            "message": "Login successful",
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": "1 hour"
        }

    except HTTPException as e:

        raise e

    except SQLAlchemyError:

        raise HTTPException(
            status_code=500,
            detail="Database connection error"
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to login"
        )

# ============================================================
# ✅ CREATE BOOK
# ============================================================

@app.post("/books")
def create_book(
    book: Book,
    user: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    '''
    Depends(verify_token)

    Means:
    Before API executes:
        verify_token() runs first

    If token invalid:
        API stops immediately
    '''

    try:

        # Check duplicate ID
        existing_book = db.query(BookDB).filter(
            BookDB.id == book.id
        ).first()

        if existing_book:

            raise HTTPException(
                status_code=400,
                detail="Book ID already exists"
            )

        # Check duplicate title
        existing_title = db.query(BookDB).filter(
            BookDB.title == book.title
        ).first()

        if existing_title:

            raise HTTPException(
                status_code=400,
                detail="Book title already exists"
            )

        # Add book
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
            "message": "Book created",
            "data": new_book
        }

    except HTTPException as e:

        raise e

    except SQLAlchemyError:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Unable to insert data into database"
        )

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Something went wrong while creating book"
        )

# ============================================================
# ✅ READ ALL BOOKS
# ============================================================

@app.get("/books")
def get_all_books(
    user: str = Depends(verify_token),
    db: Session = Depends(get_db)
):

    '''
    Flow While Calling This API:

    1. Read Authorization Header
    2. Extract Bearer Token
    3. verify_token() runs
    4. jwt.decode() validates:
        - Secret key
        - Expiry
        - Algorithm
    5. If valid:
        Continue API
    6. If expired:
        Return 401 Error
    '''

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
# ✅ READ SINGLE BOOK
# ============================================================

@app.get("/books/{book_id}")
def get_book(
    book_id: int,
    user: str = Depends(verify_token),
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

        return book

    except HTTPException as e:

        raise e

    except Exception:

        raise HTTPException(
            status_code=500,
            detail="Unable to fetch book"
        )

# ============================================================
# ✅ UPDATE BOOK
# ============================================================

@app.put("/books/{book_id}")
def update_book(
    book_id: int,
    updated_book: Book,
    user: str = Depends(verify_token),
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
        book.published_year = updated_book.published_year
        book.available = updated_book.available

        db.commit()

        db.refresh(book)

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
    user: str = Depends(verify_token),
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


