from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .students_courses import students_courses

from contract.db_orm import Base


# Визначення моделі даних (таблиці) за допомогою класу
class StudentsORM(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    courses = relationship(
        "CoursesORM",
        secondary=students_courses,
        back_populates="students"
    )


