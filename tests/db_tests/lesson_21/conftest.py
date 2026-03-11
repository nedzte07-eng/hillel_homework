import psycopg2
import os

import pytest
from dotenv import load_dotenv
load_dotenv()
# Параметри підключення
# База даних повинна існувати на зазначеному хості, та юзер повинен мати право на читання цього запису



@pytest.fixture(scope="session")
def connect_db():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DB01_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        print("Connected to the database successfully!")

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    yield connection

    connection.close()
    print("PostgreSQL connection is closed")

@pytest.fixture(scope="function")
def cursor(connect_db):
    # Для виконання запитів ви можете створити курсор
    cursor = connect_db.cursor()
    # Для виконання SQL запитів ви можете викликати метод execute() курсора
    # Тут можна виконати будь який запит на мові SQL, і він виконається в БД
    cursor.execute("SELECT version();")
    # Отримання результатів запиту
    record = cursor.fetchone()
    print("You are connected to - ", record)

    yield cursor
    connect_db.rollback()
    cursor.close()

@pytest.fixture(scope="function")
def cursor_con(connect_db):
    # Для виконання запитів ви можете створити курсор
    cursor = connect_db.cursor()
    # Для виконання SQL запитів ви можете викликати метод execute() курсора
    # Тут можна виконати будь який запит на мові SQL, і він виконається в БД
    cursor.execute("SELECT version();")
    # Отримання результатів запиту
    record = cursor.fetchone()
    print("You are connected to - ", record)

    yield cursor, connect_db
    connect_db.rollback()
    cursor.close()
