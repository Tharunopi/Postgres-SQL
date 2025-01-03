CREATE TABLE department(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	department VARCHAR(5) 
)

SELECT * FROM deps

INSERT INTO department(name, department)
VALUES 
	('Tharun', 'A'),
	('Atithya', 'A'),
	('Op', 'B')

SELECT 
SUM(CASE WHEN department = 'A' THEN 1 ELSE 0 END) / SUM(CASE WHEN department = 'B' THEN 1 ELSE 0 END) AS ratio
FROM department

ALTER TABLE department
RENAME TO deps

DELETE FROM deps 
WHERE department = 'B'