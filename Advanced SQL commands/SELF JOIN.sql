-- SELECT a.first_name, a.last_name FROM customer AS a
-- JOIN customer AS b ON
-- a.customer_id = b.customer_id

-- SELECT a.title AS film_1, b.title AS film_2, b.length AS length FROM film AS a
-- JOIN film AS b 
-- ON a.length = b.length AND a.film_id != b.film_id

SELECT length, COUNT(length) FROM film
GROUP BY length
ORDER BY COUNT(length) DESC