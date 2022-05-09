from dependency_injector import containers, providers
from app.server.services.StudentService import StudentService

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(packages=["app.server.controllers"])
    config = providers.Configuration()

    student_service = providers.Factory(
        StudentService
    )
