from fastapi import FastAPI
from typing import List
from models import Student  # Import du modèle Student
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Add CORS middleware to allow requests from your Next.js app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your Next.js frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base de données temporaire
students: List[Student] = [
    Student(id='1', name="Alice", age=22, course="Math"),
    Student(id='2', name="Bob", age=24, course="Physics"),

]

# Route pour récupérer tous les étudiants
@app.get("/students/")
def get_students():
    return students

# Route pour ajouter un étudiant
@app.post("/students/")
def create_student(student: Student):
    students.append(student)
    return student

# Route pour récupérer un étudiant par ID
@app.get("/students/{student_id}")
def get_student(student_id: str):
    for student in students:
        if student.id == student_id:
            return student
    return {"error": "Student not found"}

# Route pour supprimer un étudiant
@app.delete("/students/{student_id}")
def delete_student(student_id: str):
    global students
    students = [student for student in students if student.id != student_id]
    return {"message": "Student deleted"}