-- SELECT payment.customer_id, customer.email, amount FROM payment
-- INNER JOIN customer
-- ON payment.customer_id = customer.customer_id
-- WHERE amount > (SELECT AVG(amount) FROM payment)

-- SELECT * FROM customer
-- WHERE activebool = true

-- SELECT AVG(amount) FROM payment 
-- WHERE amount > (SELECT AVG(amount) FROM payment)
-- ORDER BY AVG(amount) DESC

-- SELECT * FROM film 
-- WHERE film_id IN (SELECT film_id FROM rental
-- INNER JOIN inventory
-- ON rental.inventory_id = inventory.inventory_id
-- WHERE return_date BETWEEN '2005-06-01' AND '2005-07-01')

SELECT first_name, last_name FROM customer 
WHERE exists
(SELECT customer_id FROM payment 
WHERE payment.customer_id = customer.customer_id AND amount > 11)