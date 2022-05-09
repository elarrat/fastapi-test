from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder
from dependency_injector.wiring import inject, Provide
from app.container import Container
from app.server.models.dtos.CreateStudentRequestDto import CreateStudentRequestDto
from app.server.services.StudentService import StudentService

router = APIRouter()

@inject
@router.post("/", response_description="Student data added into the database")
async def add_student_data(
    body: CreateStudentRequestDto = Body(...), 
    service: StudentService = Depends(Provide[Container.student_service])
):
    body = jsonable_encoder(body)
    new_student = service.create(body)
    return new_student