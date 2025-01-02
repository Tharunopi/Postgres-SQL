CREATE TABLE job_user(
	user_id INTEGER REFERENCES user_accounts(user_id),
	job_id INTEGER REFERENCES jobs(job_id),
	hire_date TIMESTAMP
)