-- get rows only unique to left table

-- SELECT first_name, customer.customer_id FROM payment
-- LEFT OUTER JOIN customer
-- ON payment.customer_id = customer.customer_id
-- WHERE customer.customer_id IS null

SELECT film.film_id, film.title, inventory_id FROM film
LEFT OUTER JOIN inventory
ON film.film_id = inventory.film_id
WHERE inventory.film_id IS null