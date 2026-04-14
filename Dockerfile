# Використовуй один базовий образ, а не два поспіль
FROM python:3.14

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо код
COPY . /app

# Встановлюємо залежності
RUN pip install pytest psycopg2

# Змінні середовища для Postgres краще не прописувати тут,
# а передавати через docker-compose.yml або docker run -e
# Якщо все ж потрібно залишити тут — можна додати hadolint ignore:
# hadolint ignore=DL3005
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=569300
ENV POSTGRES_DB=postgres

# Команда за замовчуванням
CMD ["pytest", "tests/lesson_29/test_lesson_29.py"]
