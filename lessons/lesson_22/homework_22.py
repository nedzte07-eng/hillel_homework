import os
import random
from faker import Faker

from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from contract.db_orm import Base
from contract.db_orm.students_courses import students_courses
from contract.db_orm.courses_orm import CoursesORM
from contract.db_orm.students_orm import StudentsORM

load_dotenv()

dbname = os.getenv("DB01_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")

# З'єднання з базою даних PostgreSQL (замініть дані на ваші)
DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
engine = create_engine(DATABASE_URL)


def table_drop(orm_class_or_table, engine_for_drop):
    inspector = inspect(engine_for_drop)
    if hasattr(orm_class_or_table, "__tablename__"):
        table_name = orm_class_or_table.__tablename__
        table_obj = orm_class_or_table.__table__
    else:
        table_name = orm_class_or_table.name
        table_obj = orm_class_or_table

    if inspector.has_table(table_name):
        table_obj.drop(engine_for_drop)
        print(f"Dropped table '{table_name}'")
    else:
        print(f"Table '{table_name}' does not exist")


def random_courses_string():
    length = random.randint(1, 4)
    ids = random.sample(range(1, 6), length)
    return str(", ".join(map(str, ids)))


print(random_courses_string())

table_drop(students_courses, engine)
table_drop(StudentsORM, engine)
table_drop(CoursesORM, engine)

# Створення таблиці у базі даних
Base.metadata.create_all(engine)

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

astronomy = CoursesORM(course_name='Astronomy')
biology = CoursesORM(course_name='Biology')
chemistry = CoursesORM(course_name='Chemistry')
physics = CoursesORM(course_name='Physics')
art = CoursesORM(course_name='Art')

list_of_courses = [astronomy, biology, chemistry, physics, art]

list_of_students = []
count = 0
fake = Faker()
while count < 20:
    student = StudentsORM(name=fake.first_name(), age=random.randint(18, 24),
                          courses=random.sample(list_of_courses, random.randint(1, len(list_of_courses))))
    list_of_students.append(student)
    count += 1

tables_list = list_of_courses + list_of_students

session.add_all(tables_list)
session.commit()


def students_on_course(name_of_course):
    course = session.query(CoursesORM).filter_by(course_name=name_of_course).first()
    print(f'On the course {name_of_course} there are such students:')
    for student in course.students:
        print(student.name)


def courses_of_the_student(student_id):
    student_check = session.get(StudentsORM, student_id)
    print(f'For the student with id {student_id} and name {student_check.name} there are such courses:')
    for course in student_check.courses:
        print(course.course_name)


def add_new_student(student_name, student_age, student_courses):
    new_student = StudentsORM(name=student_name, age=student_age, courses=student_courses)
    session.add(new_student)
    session.commit()


def update_student(student_id, new_name=None, new_age=None, new_courses=None):
    changed_student = session.get(StudentsORM, student_id)

    if new_name:
        changed_student.name = new_name

    if new_age:
        changed_student.age = new_age

    if new_courses:
        changed_student.courses = new_courses

    session.commit()
    print(f"Студент {student_id} оновлений")
    return changed_student


def delete_student(student_id):
    student_to_delete = session.get(StudentsORM, student_id)
    session.delete(student_to_delete)
    session.commit()
    print(f"Студент з id={student_id} і ім'ям {student_to_delete.name} видалений")
    return student_to_delete


add_new_student('Sasha', 41, [astronomy, art])

update_student(student_id=12, new_name='Masha', new_age=70, new_courses=[art, chemistry])

delete_student(student_id=15)

students_on_course('Art')

courses_of_the_student(10)

session.close()
