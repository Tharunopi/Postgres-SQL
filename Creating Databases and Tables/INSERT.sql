INSERT INTO user_accounts(username, email, password, created_on)
VALUES 
	('Tharun', 'tharunaadhi@gmail.com', 'password', CURRENT_TIMESTAMP),
	('Atithya', 'atithya@gmail.com', 'password', CURRENT_TIMESTAMP)

SELECT * FROM user_accounts

INSERT INTO jobs(job_name)
VALUES 
	('ML ENGINEER'),
	('ASTRONUT'),
	('TOP-G')

SELECT * FROM jobs

INSERT INTO job_user(user_id, job_id, hire_date)
VALUES 
	(1, 3, CURRENT_TIMESTAMP),
	(2, 1, CURRENT_TIMESTAMP), 
	(1, 2, CURRENT_TIMESTAMP)

SELECT * FROM job_user