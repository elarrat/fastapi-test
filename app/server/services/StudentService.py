from app.server.database import db

from app.server.models.dtos.CreateStudentRequestDto import CreateStudentRequestDto
from app.server.repositories.StudentRepo import StudentRepo

class StudentService:
    def create(self, student: CreateStudentRequestDto):
        repo = StudentRepo(db)
        result = repo.add_student(student)
        return self.student_helper(result)

    def student_helper(self, student) -> dict:
        return {
            "id": str(student["_id"]),
            "fullname": student["fullname"],
            "email": student["email"],
            "course_of_study": student["course_of_study"],
            "year": student["year"],
            "GPA": student["gpa"],
        }