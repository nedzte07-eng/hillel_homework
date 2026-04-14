import psycopg2

def test_database_connection(db_conn):
    conn = db_conn
    assert conn is not None

def test_insert_data(cursor_con):
    cursor, db_conn = cursor_con
    cursor.execute("INSERT INTO lesson29 (id, name, city, phone) VALUES (4, 'Pasha', 'Jitomir', '555-66-77')")
    db_conn.commit()
    cursor.execute("SELECT * FROM lesson29 WHERE phone = '555-66-77'")
    result = cursor.fetchone()
    assert result[1] == 'Pasha'

def test_edit_data(cursor_con):
    cursor, db_conn = cursor_con
    cursor.execute("UPDATE public.lesson29 SET city = 'Mukachevo' WHERE name = 'Pasha'")
    db_conn.commit()
    cursor.execute("SELECT city FROM public.lesson29 WHERE name = 'Pasha'")
    result = cursor.fetchone()
    assert result[0] == 'Mukachevo'

def test_delete_data(cursor_con):
    cursor, db_conn = cursor_con
    cursor.execute("DELETE FROM public.lesson29 WHERE name = 'Pasha'")
    db_conn.commit()
    cursor.execute("SELECT * FROM public.lesson29 WHERE name = 'Pasha'")
    result = cursor.fetchone()
    assert result is None

# def test_database_connection():
#     conn = psycopg2.connect(
#         dbname="postgres",
#         user="postgres",
#         password="569300",
#         host="db",  # ім'я сервісу з docker-compose
#         port=5432
#     )
#     assert conn is not None
#
# def test_insert_data():
#     conn = psycopg2.connect(
#         dbname="postgres",
#         user="postgres",
#         password="569300",
#         host="host.docker.internal",  # ім'я сервісу з docker-compose
#         port=5432
#     )
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO public.lesson29 (id, name, city, phone) VALUES (4, 'Pasha', 'Jitomir', '555-66-77')")
#     conn.commit()
#     cursor.execute("SELECT * FROM public.lesson29 WHERE phone = '555-66-77'")
#     result = cursor.fetchone()
#     assert result[1] == 'Pasha'

