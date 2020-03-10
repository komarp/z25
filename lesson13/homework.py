import psycopg2

"""
Описать для каждой таблицы из домашки(lesson12) класс,
который позволяет взаимодействовать с конткретной таблицей

Пример:
class User:
    ...
    def get_users(user_id=None, username=None):
        ...
    def create_users(*users_list):
        ...

class Test:
    ...

и тд
"""


class SQL:
    def __init__(self, table_name):
        self.table_name = table_name

    def sql_reader(self, *args):
        dsn = 'postgres://pasha:q07042001q@localhost:5432/mydb'
        conn = psycopg2.connect(dsn=dsn)
        cur = conn.cursor()
        if not args:
            cur.execute('SELECT * FROM %s;' % self.table_name)
            return cur.fetchall()
        cur.execute('SELECT %s FROM %s;' % (','.join(args), self.table_name))
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def sql_writer(self, *column_order, **content):
        dsn = 'postgres://pasha:q07042001q@localhost:5432/mydb'
        conn = psycopg2.connect(dsn=dsn)
        conn.autocommit = True
        cursor = conn.cursor()
        _str = ""
        for value in content.values():
            if isinstance(value, str):
                _str += f"'{value}'" if not len(_str) else f", '{value}'"
            else:
                _str += f"{value}" if not len(_str) else f", {value}"
        cursor.execute(f"""INSERT INTO {self.table_name} ({', '.join(column_order)})
VALUES ({_str});""")
        cursor.close()
        conn.close()

    def sql_deleter(self, condition):
        dsn = 'postgres://pasha:q07042001q@localhost:5432/mydb'
        conn = psycopg2.connect(dsn=dsn)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute("DELETE FROM %s WHERE %s;" % (self.table_name, condition))
        cur.close()
        conn.close()
