CREATE TABLE information(
	info_id SERIAL PRIMARY KEY,
	title VARCHAR(500) NOT NULL,
	person_name VARCHAR(50) NOT NULL UNIQUE
)

SELECT * FROM new_info

ALTER TABLE new_info
RENAME COLUMN person_name TO bankai

ALTER TABLE new_info
ALTER COLUMN bankai DROP NOT NULL

INSERT INTO new_info(title)
VALUES 
	('jjba')