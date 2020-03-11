from datetime import datetime

from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Integer,
    String,
    DateTime
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'postgres://postgres:postgres@localhost:5432/sqlalchemy'
)
metadata = MetaData()

BaseModel = declarative_base(bind=engine)


class Question(BaseModel):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=True)
    text = Column(String)
    created_at = Column(DateTime, default=datetime.now)

    def __str__(self):
        return f'{self.id} {self.number} {self.text} {self.created_at}'
    __repr__ = __str__


BaseModel.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
