CREATE TABLE teachers(
	teacher_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50),
	homeroom_number INTEGER NOT NULL,
	department VARCHAR(50) NOT NULL,
	email VARCHAR(200) NOT NULL UNIQUE,
	phone VARCHAR(20) NOT NULL UNIQUE
)

CREATE TABLE students(
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50),
	homeroom_number INTEGER NOT NULL,
	phone VARCHAR(20) NOT NULL UNIQUE,
	email VARCHAR(200) NOT NULL UNIQUE,
	graduation_year INTEGER NOT NULL
)

SELECT * FROM teachers
SELECT * FROM students

INSERT INTO students(first_name, last_name, homeroom_number, phone, email, graduation_year)
VALUES 
	('Mark', 'Watney', 5, '777-555-1234', null, 2035)

ALTER TABLE students
ALTER COLUMN email DROP NOT NULL

INSERT INTO teachers(first_name, last_name, homeroom_number, department, email, phone)
VALUES 
	('Jonas', 'Salk', 5, 'Biology', 'jsalk@school.org', '777-555-4321')