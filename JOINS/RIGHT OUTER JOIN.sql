SELECT * FROM inventory
RIGHT OUTER JOIN film
ON inventory.film_id = film.film_id
WHERE inventory.inventory_id IS null