# Step 1: Import Libraries
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Step 2: Create App
app = FastAPI()

# Step 3: Create Data Model (Schema)
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str
    marks: int

# Step 4: Temporary Database
students = []

# ==================================================
# 1. Create Student (POST)
# ==================================================
@app.post("/students")
def create_student(student: Student):

    students.append(student)

    return {
        "message": "Student added successfully",
        "data": student
    }

# ==================================================
# 2. Read All Students (GET)
# ==================================================
@app.get("/students")
def get_students():

    return students

# ==================================================
# 3. Read Single Student (GET by ID)
# ==================================================
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:

        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# ==================================================
# 4. Update Student (PUT)
# ==================================================
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for index, student in enumerate(students):

        if student.id == student_id:

            students[index] = updated_student

            return {
                "message": "Updated successfully",
                "data": updated_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# ==================================================
# 5. Delete Student (DELETE)
# ==================================================
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for index, student in enumerate(students):

        if student.id == student_id:

            deleted_student = students.pop(index)

            return {
                "message": "Deleted successfully",
                "data": deleted_student
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
