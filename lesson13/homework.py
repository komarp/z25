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
import psycopg2
from psycopg2.extras import execute_values


def eq(column_name, value):
    return f'{column_name} = {value}'


def or_(*conditions):
    return ' OR '.join(conditions)


class Connection:
    def __init__(
            self,
            username,
            password,
            db_name,
            host='localhost',
            port=5432,
    ):
        self.dsn = f'postgres://{username}:{password}@{host}:{port}/{db_name}'

    def open(self):
        return psycopg2.connect(self.dsn)


connection = Connection(
    username='postgres',
    password='postgres',
    db_name='homework'
)


class BaseModel:
    table_name = None
    columns = tuple()
    insert_exclude_columns = {'id'}
    connection = connection

    def __init__(self, **kwargs):
        for column in self.columns:
            setattr(self, column, kwargs.get(column))

    @classmethod
    def get_insert_columns(cls):
        return tuple(filter(
            lambda x: x not in cls.insert_exclude_columns,
            cls.columns)
        )

    @classmethod
    def to_list(cls, obj):
        result = []
        for column in cls.get_insert_columns():
            result.append(getattr(obj, column, None))
        return result

    @classmethod
    def select(cls, columns=None, filter_query=''):
        columns = columns or cls.columns
        if filter_query:
            filter_query = f'WHERE {filter_query}'
        with cls.connection.open() as con:
            with con.cursor() as cursor:
                columns_str = ','.join(columns)
                query = f"""SELECT {columns_str} FROM {cls.table_name} {filter_query};"""  # noqa
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    yield cls(**dict(zip(columns, row)))

    @classmethod
    def insert(cls, *objects):
        for_insert = []
        for _object in objects:
            for_insert.append(cls.to_list(_object))
        with cls.connection.open() as con:
            with con.cursor() as cursor:
                columns_str = ','.join(cls.get_insert_columns())
                execute_values(
                    cursor,
                    f"INSERT INTO {cls.table_name} ({columns_str}) VALUES %s;",
                    for_insert
                )

    @classmethod
    def delete(cls, filter_query=''):
        if filter_query:
            filter_query = f'WHERE {filter_query}'
        with cls.connection.open() as con:
            with con.cursor() as cursor:
                cursor.execute(f'DELETE FROM {cls.table_name} {filter_query};')

    def __str__(self):
        _str = ''
        for column in self.columns:
            _str += f'{column}: {getattr(self, column)} |'
        return _str

    __repr__ = __str__


class Tests(BaseModel):
    table_name = 'tests'
    columns = ('id', 'number', 'text')


class Question(BaseModel):
    table_name = 'questions'
    columns = ('id', 'text')
