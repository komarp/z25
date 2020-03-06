CREATE TABLE app_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE tests (
    id SERIAL PRIMARY KEY,
    number SMALLINT NOT NULL,
    text VARCHAR(30) NOT NULL
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    number SMALLINT NOT NULL,
    text VARCHAR(30) NOT NULL
);

CREATE TABLE tests_questions (
    id SERIAL PRIMARY KEY,
    test_id INTEGER REFERENCES tests(id),
    question_id INTEGER REFERENCES questions(id),
    UNIQUE (test_id, question_id)
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    number SMALLINT NOT NULL,
    text VARCHAR(30) NOT NULL,
    is_correct BOOL DEFAULT FALSE
);

CREATE TABLE users_answers (
    id SERIAL PRIMARY KEY,
    tests_questions_id INTEGER REFERENCES tests_questions(id),
    user_id INTEGER REFERENCES app_users(id),
    answer_id INTEGER REFERENCES answers(id),
    UNIQUE (tests_questions_id, user_id)
);


