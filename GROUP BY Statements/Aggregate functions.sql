SELECT SUM(rental_rate) FROM film
WHERE rating NOT IN('R', 'PG-13') 