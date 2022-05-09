class StudentRepo:
    def __init__(self, db) -> None:
        self.db = db        
        
    def add_student(self, student_data: dict) -> dict:
        self.db.students.insert_one(student_data)
        return student_data