FROM python:3.14

WORKDIR /app

COPY . /app

RUN pip install pytest \
    && pip install python-dotenv \
    && pip install playwright \
    && pip install pytest-playwright

# Встановлення браузерів
RUN playwright install --with-deps chromium

CMD ["pytest",  "tests/lesson_28_2/test_lesson_28_2.py"]