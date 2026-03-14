import os
import random

from dotenv import load_dotenv
from sqlalchemy import create_engine, func, inspect
from sqlalchemy.orm import sessionmaker

from contract.db_orm import Base
from contract.db_orm.students_courses import students_courses
from contract.db_orm.courses_orm import CoursesORM
from contract.db_orm.students_orm import StudentsORM

load_dotenv()



dbname=os.getenv("DB01_NAME")
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")
host=os.getenv("DB_HOST")
port=os.getenv("DB_PORT")

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
student1 = StudentsORM(name='John', age=random.randint(18, 24), courses=[astronomy, chemistry] )

session.add_all([astronomy, biology, chemistry, physics, art, student1])
session.commit()
# SQL аналог:
# INSERT INTO users (name, age) VALUES ('John', 30), ('Alice', 25), ('Bob', 35);
#
# # Використання виразів для складного запиту: обчислення середнього віку користувачів
# average_age = session.query(func.avg(StudentsORM.age)).scalar()
# print("Середній вік користувачів:", average_age)
# # SQL аналог: SELECT AVG(age) FROM users;
#
# # Використання виразів для складного запиту: підрахунок кількості користувачів
# user_count = session.query(func.count(StudentsORM.id)).scalar()
# print("Кількість користувачів:", user_count)
# # SQL аналог: SELECT COUNT(id) FROM users;
#
# Закриття сесії
session.close()