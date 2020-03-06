CREATE TABLE test_id(
	test_id SERIAL PRIMARY KEY,
	test_name VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE right_ans_table(
	test_id INT REFERENCES test_id (test_id),
	num_of_q INT CHECK(0 < num_of_q and num_of_q < 8) PRIMARY KEY,
	right_answer INT CHECK(0 < right_answer and right_answer < 4));

CREATE TABLE users(
	user_id SERIAL PRIMARY KEY,
	login VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE answers(
	id SERIAL PRIMARY KEY,
	user_id INT REFERENCES users(user_id),
	test_id INT REFERENCES test_id(test_id),
	num_of_q INT REFERENCES right_ans_table(num_of_q),
	answer INT CHECK(answer > 0 and answer < 5)
);

