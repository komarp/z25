CREATE TABLE app_user (
    id SERIAL PRIMARY KEY,
    email VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE topic (
    id SERIAL PRIMARY KEY,
    name VARCHAR (60) NOT NULL,
    user_id INTEGER references app_user(id)
);

CREATE TABLE message (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    user_id INTEGER references app_user(id),
    topic_id INTEGER references topic(id)
);

