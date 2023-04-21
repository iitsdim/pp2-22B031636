import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="phonebook",
    user="postgres",
    password="dimash"
)


def insert_inside_phone_book(cursor, username, phone):
    prefix = "INSERT INTO phone_book (username, phone) VALUES (%s, %s) RETURNING id;"
    cursor.execute(prefix, (username, phone))
    return cursor.fetchone()[0]
