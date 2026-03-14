from sqlalchemy import Column, Integer, ForeignKey, Table
from . import Base

students_courses = Table(
    "students_courses",
    Base.metadata,
Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
)
