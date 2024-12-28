-- SELECT customer.first_name, customer.email, address.district FROM address
-- INNER JOIN customer 
-- ON customer.address_id = address.address_id
-- WHERE address.district = 'California'

SELECT actor.first_name, actor.last_name, title FROM actor
INNER JOIN film_actor 
ON film_actor.actor_id = actor.actor_id
INNER JOIN film
ON film.film_id = film_actor.film_id
WHERE actor.first_name = 'Nick' AND actor.last_name = 'Wahlberg'