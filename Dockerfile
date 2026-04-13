FROM python:3.14

WORKDIR /app

COPY . /app

RUN pip install pytest \
    && pip install psycopg2



CMD ["pytest",  "tests/lesson_29/test_lesson_29.py"]