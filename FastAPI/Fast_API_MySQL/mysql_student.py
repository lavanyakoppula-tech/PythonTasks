# ============================================================
# 🎓 FastAPI Student CRUD App (SQLite Version)
# pip install fastapi uvicorn sqlalchemy
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session


# ------------------------------------------------------------
# 🚀 App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🗄️ MySQL Configuration
# ------------------------------------------------------------
DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/student_db"

'''
mysql+pymysql://root:root@localhost:3306/student_db
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

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()



# ------------------------------------------------------------
# 🧱 Student Table
# ------------------------------------------------------------
class StudentDB(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    age = Column(Integer)
    course = Column(String(255))
    marks = Column(Integer)

# Create Table
Base.metadata.create_all(bind=engine)

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str
    marks: int

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
        "message": "Student Management System with SQLite 🚀"
    }

# ------------------------------------------------------------
# ✅ CREATE STUDENT
# ------------------------------------------------------------
@app.post("/students")
def create_student(
    student: Student,
    db: Session = Depends(get_db)
):

    existing = db.query(StudentDB).filter(
        StudentDB.id == student.id
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    new_student = StudentDB(
        id=student.id,
        name=student.name,
        age=student.age,
        course=student.course,
        marks=student.marks
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return {
        "message": "Student created successfully",
        "data": new_student
    }

# ------------------------------------------------------------
# ✅ GET ALL STUDENTS
# ------------------------------------------------------------
@app.get("/students")
def get_students(
    db: Session = Depends(get_db)
):

    students = db.query(StudentDB).all()

    return {
        "count": len(students),
        "data": students
    }

# ------------------------------------------------------------
# ✅ GET STUDENT BY ID
# ------------------------------------------------------------
@app.get("/students/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

# ------------------------------------------------------------
# ✅ UPDATE STUDENT
# ------------------------------------------------------------
@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    updated_student: Student,
    db: Session = Depends(get_db)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = updated_student.name
    student.age = updated_student.age
    student.course = updated_student.course
    student.marks = updated_student.marks

    db.commit()

    db.refresh(student)

    return {
        "message": "Student updated successfully",
        "data": student
    }

# ------------------------------------------------------------
# ✅ DELETE STUDENT
# ------------------------------------------------------------
@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(StudentDB).filter(
        StudentDB.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)

    db.commit()

    return {
        "message": "Student deleted successfully"
    }


