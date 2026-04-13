# import pytest
# import psycopg2
#
#
# @pytest.fixture(scope="session")
# def db_conn():
#     conn = psycopg2.connect(
#         dbname="lesson29",
#         user="postgres",
#         password="569300",
#         host="db",  # ім'я сервісу з docker-compose
#         port=5432
#     )
#     yield conn
#     conn.close()
#
#
# @pytest.fixture(scope="function")
# def cursor_con(db_conn):
#     cursor = db_conn.cursor()
#     yield cursor, db_conn
#     db_conn.rollback()
#     cursor.close()
