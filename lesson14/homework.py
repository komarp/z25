from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Integer,
    String,
    Sequence,
    ForeignKey,
    UniqueConstraint,
    Boolean
)
from sqlalchemy.ext.declarative import declarative_base

"""Описать таблицы из lesson12/homework.sql при помощи sqlalchemy"""

engine = create_engine(
    'postgres://pasha:q07042001q@localhost:5432/homework'
)

metadata = MetaData()

Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = 'app_users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(30), nullable=False)

    def __str__(self):
        return "User(id = '%s', username = '%s')" % (self.id, self.username)

    __repr__ = __str__


class Test(Base):
    __tablename__ = 'tests'

    id = Column(Integer, Sequence('test_id_seq'), primary_key=True)
    number = Column(Integer, nullable=False)
    text = Column(String(100), nullable=False)

    def __str__(self):
        return "Test(id = '%s', number = '%s', text = '%s')" % (
            self.id, self.number, self.text
        )

    __repr__ = __str__


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, Sequence('question_id_seq'), primary_key=True)
    number = Column(String, nullable=False)
    text = Column(String(100), nullable=False)

    def __str__(self):
        return "Question(id = '%s', number = '%s', text = '%s')" % (
            self.id, self.number, self.text
        )

    __repr__ = __str__


class TestQuestion(Base):
    __tablename__ = 'tests_questions'

    id = Column(Integer, Sequence('test_question_id_seq'), primary_key=True)
    test_id = Column(Integer, ForeignKey('tests.id'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    __table_args__ = (UniqueConstraint('test_id', 'question_id', name='_test_question_uc'),
                      )

    def __str__(self):
        return "TestQuestion(id = '%s', test_id = '%s', question_id = '%s')" % (
            self.id, self.test_id, self.question_id
        )

    __repr__ = __str__


class Answer(Base):
    __tablename__ = 'answers'

    id = Column(Integer, Sequence('answer_id_seq'), primary_key=True)
    text = Column(String(100), nullable=False)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey('questions.id'))

    def __str__(self):
        return "Answer(id = '%s', text = '%s', is_correct = '%s', question_id = '%s')" % (
            self.id, self.text, self.is_correct, self.question_id
        )

    __repr__ = __str__


class UserAnswer(Base):
    __tablename__ = 'users_answers'

    id = Column(Integer, Sequence('user_answer_seq'), primary_key=True)
    tests_questions_id = Column(Integer, ForeignKey('tests_questions.id'))
    user_id = Column(Integer, ForeignKey('app_users.id'))
    answer_id = Column(Integer, ForeignKey('answers.id'))
    __table_args__ = (UniqueConstraint('tests_questions_id', 'user_id', name='test_user_id_uc'), )

    def __str__(self):
        return "UserAnswer(id = '%s', tests_questions_id = '%s', user_id = '%s'," \
               "answer_id = '%s')" % (self.id, self.tests_questions_id, self.user_id,
                                      self.answer_id)
    __repr__ = __str__


Base.metadata.create_all(engine)