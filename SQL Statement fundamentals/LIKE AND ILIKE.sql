-- SELECT first_name FROM customer
-- WHERE first_name LIKE '_her%'

SELECT COUNT(first_name) FROM customer
WHERE first_name ILIKE 'J%'