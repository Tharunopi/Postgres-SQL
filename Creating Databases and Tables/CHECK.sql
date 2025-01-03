CREATE TABLE employee(
	emp_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50),
	birthdate DATE CHECK(birthdate > '2000-01-01'),
	hiredate DATE CHECK(hiredate > birthdate)
)

ALTER TABLE employee
ADD COLUMN salary INTEGER CHECK(salary > 0)

ALTER TABLE employee
ALTER COLUMN salary SET NOT NULL

SELECT * FROM employee

INSERT INTO employee(first_name, last_name, birthdate, hiredate, salary)
VALUES 
	('Tharun', null, '2003-11-26', '2024-10-23', 50000)