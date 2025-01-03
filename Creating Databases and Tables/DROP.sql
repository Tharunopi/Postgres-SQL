SELECT * FROM new_info

INSERT INTO new_info(title)
VALUES 
	('bleach'),
	('bleach tybw')

ALTER TABLE new_info
ADD COLUMN bankai VARCHAR(50) UNIQUE

UPDATE new_info
	SET 
		bankai = title || '.bankai'
	WHERE title LIKE '%bleach%'