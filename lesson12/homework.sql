CREATE TABLE app_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(30) UNIQUE NOT NULL
);

CREATE TABLE tests (
    id SERIAL PRIMARY KEY,
    number SMALLINT NOT NULL,
    text VARCHAR(100) NOT NULL
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    number SMALLINT NOT NULL,
    text VARCHAR(100) NOT NULL
);

CREATE TABLE tests_questions (
    id SERIAL PRIMARY KEY,
    test_id INTEGER REFERENCES tests(id),
    question_id INTEGER REFERENCES questions(id),
    UNIQUE (test_id, question_id)
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    text VARCHAR(100) NOT NULL,
    is_correct BOOL DEFAULT FALSE,
    question_id INTEGER REFERENCES questions(id)
);

CREATE TABLE users_answers (
    id SERIAL PRIMARY KEY,
    tests_questions_id INTEGER REFERENCES tests_questions(id),
    user_id INTEGER REFERENCES app_users(id),
    answer_id INTEGER REFERENCES answers(id),
    UNIQUE (tests_questions_id, user_id)
);


INSERT INTO tests (number, text)
VALUES (1, 'Test 1'),
       (2, 'Test 2'),
       (3, 'Test 3');

INSERT INTO questions (number, text)
VALUES (1, 'Какое растение существует на самом деле?'),
       (2, 'Что за место, попав в которое, человек делает селфи на кухне, ' ||
        'которую не может себе позволить?'),
       (3, 'Что проводит боксер, наносящий удар противнику снизу?'),
       (4, 'Как называется ближайшая к Земле звезда?'),
       (5, 'Что помогает запомнить мнемоническое правило «Это я знаю и помню ' ||
        'прекрасно»?'),
       (6, 'Какую площадь имеет клетка стандартной школьной тетради?'),
       (7, 'Как назывались старинные русские пушки-гаубицы?');


INSERT INTO tests_questions (test_id, question_id)
VALUES
(1, 1),
(1, 2),
(1, 3),
(1, 4),
(1, 5),
(2, 1),
(2, 4),
(2, 5),
(3, 7),
(3, 6),
(3, 5)
;

INSERT INTO answers(text, is_correct, question_id)
VALUES ('Лох чилийский', false, 1),
       ('Лох индийский', true, 1),
       ('Лох греческий', false, 1),
       ('Лох русский', false, 1),
       ('Лондон', false, 2),
       ('Париж', false, 2),
       ('Рим', false,2),
       ('Икеа', true, 2),
       ('Свинг', false, 3),
       ('Хук', false, 3),
       ('Апперкот', true, 3),
       ('Джэб', false, 3),
       ('Проксиома Центавра', false, 4),
       ('Солнце', true, 4),
       ('Полярная', false, 4),
       ('Сириус', false, 4),
       ('Число Пи', true, 5),
       ('Ряд активности металлов', false, 5),
       ('Цвета радуги', false, 5),
       ('Порядок падежей', false, 5),
       ('0.25 кв.см', true, 6),
       ('1 кв.см', false, 6),
       ('0.5 кв.см', false, 6),
       ('1.25 кв. см', false, 6),
       ('Кентавр', false, 7),
       ('Грифон', false, 7),
       ('Василиск', false, 7),
       ('Единорог', true, 7);


