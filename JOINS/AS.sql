-- SELECT first_name AS kaduvlae, last_name AS ajithey FROM customer

-- SELECT title AS thala, SUM(rental_rate) AS collection FROM film
-- GROUP BY thala

SELECT staff_id AS teacher, SUM(amount) AS collection FROM payment 
WHERE staff_id = 1
GROUP BY staff_id