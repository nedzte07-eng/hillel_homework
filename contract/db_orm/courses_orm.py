from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .students_courses import students_courses


from contract.db_orm import Base


# Визначення моделі даних (таблиці) за допомогою класу
class CoursesORM(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String, unique=True, nullable=False)

    students = relationship(
        "StudentsORM",
        secondary=students_courses,
        back_populates="courses"
    )

