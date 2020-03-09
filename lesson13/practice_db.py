import psycopg2
from psycopg2.extras import execute_values


connection = psycopg2.connect(
    dsn='postgres://postgres:postgres@localhost:5432/homework'
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM tests;")
result = cursor.fetchall()

# number = int(input('Number> '))
# text = input('Text> ')
# cursor.execute("""
# INSERT INTO tests (number, text) VALUES (%s, %s);
# """, (number, text))

execute_values(
    cursor,
    "INSERT INTO tests (number, text) VALUES %s",
    [(1, 'Test 333'), (2, 'Test 4444')]
)

connection.commit()

connection.close()


dsn = 'postgres://postgres:postgres@localhost:5432/homework'
with psycopg2.connect(dsn) as connection:
    with connection.cursor() as cursor:
        execute_values(
            cursor,
            "INSERT INTO tests (number, text) VALUES %s;",
            [(1, 'Test 111'), (2, 'Test 222')],
        )
