SELECT * FROM user_accounts
UPDATE user_accounts
	SET password = SUBSTRING(password, 0, 3) || 'ok123',
		last_appeared = CASE WHEN last_appeared IS null THEN CURRENT_TIMESTAMP
						ELSE last_appeared END
		

SELECT * FROM job_user
UPDATE job_user
	SET
		hire_date = user_accounts.created_on
	FROM user_accounts
	WHERE user_accounts.user_id = job_user.user_id
