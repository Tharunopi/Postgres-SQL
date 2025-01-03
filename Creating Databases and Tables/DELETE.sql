SELECT * FROM jobs

INSERT INTO jobs(job_name)
VALUES 
	('Coach')

DELETE FROM jobs
	WHERE job_name = 'Coach'
	RETURNING job_id, job_name