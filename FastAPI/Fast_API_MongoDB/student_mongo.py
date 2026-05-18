# ============================================================
# 🎓 FastAPI Student Management System
# MongoDB Atlas + MongoEngine
#
# Install Packages:
# pip install fastapi uvicorn mongoengine pymongo
#
# Run Server:
# uvicorn student_mongo:app --reload
# ============================================================

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import (
    connect,
    Document,
    IntField,
    StringField
)

# ------------------------------------------------------------
# 🚀 FastAPI App
# ------------------------------------------------------------
app = FastAPI()

# ------------------------------------------------------------
# 🌐 MongoDB Atlas Connection
# ------------------------------------------------------------

MONGO_URL = "mongodb+srv://lavanya_db_user:d2EpVuZm2mFknSTN@lavanya.7ovtsto.mongodb.net/student_db?retryWrites=true&w=majority"

try:

    connect(
        db="student_db",
        host=MONGO_URL
    )

    print("✅ MongoDB Atlas Connected Successfully")

except Exception as e:

    print("❌ MongoDB Connection Failed")
    print(e)

# ------------------------------------------------------------
# 🧱 MongoDB Student Model
# ------------------------------------------------------------
class StudentDB(Document):

    student_id = IntField(
        primary_key=True
    )

    name = StringField(
        required=True
    )

    age = IntField(
        required=True
    )

    course = StringField(
        required=True
    )

    marks = IntField(
        required=True
    )

    meta = {
        "collection": "students"
    }

# ------------------------------------------------------------
# 🧾 Pydantic Schema
# ------------------------------------------------------------
class Student(BaseModel):

    student_id: int
    name: str
    age: int
    course: str
    marks: int

# ------------------------------------------------------------
# 🏠 Home Route
# ------------------------------------------------------------
@app.get("/")
def home():

    return {
        "message": "FastAPI + MongoDB Atlas Student API 🚀"
    }

# ------------------------------------------------------------
# ✅ CREATE STUDENT
# ------------------------------------------------------------
@app.post("/students")
def create_student(student: Student):

    existing_student = StudentDB.objects(
        student_id=student.student_id
    ).first()

    if existing_student:

        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )

    new_student = StudentDB(
        student_id=student.student_id,
        name=student.name,
        age=student.age,
        course=student.course,
        marks=student.marks
    )

    new_student.save()

    return {
        "message": "Student created successfully",
        "data": {
            "student_id": new_student.student_id,
            "name": new_student.name,
            "age": new_student.age,
            "course": new_student.course,
            "marks": new_student.marks
        }
    }

# ------------------------------------------------------------
# ✅ GET ALL STUDENTS
# ------------------------------------------------------------
@app.get("/students")
def get_all_students():

    students = StudentDB.objects()

    data = []

    for student in students:

        data.append({
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "marks": student.marks
        })

    return {
        "count": len(data),
        "data": data
    }

# ------------------------------------------------------------
# ✅ GET SINGLE STUDENT
# ------------------------------------------------------------
@app.get("/students/{student_id}")
def get_student(student_id: int):

    student = StudentDB.objects(
        student_id=student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {
        "student_id": student.student_id,
        "name": student.name,
        "age": student.age,
        "course": student.course,
        "marks": student.marks
    }

# ------------------------------------------------------------
# ✅ UPDATE STUDENT
# ------------------------------------------------------------
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    student = StudentDB.objects(
        student_id=student_id
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

    student.save()

    return {
        "message": "Student updated successfully"
    }

# ------------------------------------------------------------
# ✅ DELETE STUDENT
# ------------------------------------------------------------
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    student = StudentDB.objects(
        student_id=student_id
    ).first()

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.delete()

    return {
        "message": "Student deleted successfully"
    }

# ============================================================
# ✅ SAMPLE JSON FOR TESTING
# ============================================================

"""
{
  "student_id": 1,
  "name": "Sai Kumar",
  "age": 24,
  "course": "Python",
  "marks": 95
}
"""
