from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import mapper, sessionmaker

engine = create_engine(
    'postgres://postgres:postgres@localhost:5432/sqlalchemy'
)

metadata = MetaData()

tests_table = Table(
    'tests',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('number', Integer, nullable=False),
    Column('text', String, nullable=False)
)

metadata.create_all(engine, tables=(tests_table,))


class Test:
    def __init__(self, number, text):
        self.number = number
        self.text = text


mapper(Test, tests_table)


Session = sessionmaker(bind=engine)
session = Session()
