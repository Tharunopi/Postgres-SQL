SELECT 
CASE 
	WHEN first_name LIKE 'J%' THEN first_name||last_name
	ELSE null
END
FROM customer

SELECT customer.customer_id, 
	CASE 
		WHEN customer_id BETWEEN 1 AND 100 THEN 'premimium customer'
		WHEN customer_id BETWEEN 101 AND 200 THEN 'silver customer'
		ELSE 'normal customer' 
	END AS customer_type
FROM customer
ORDER BY customer_id 

SELECT * FROM film

SELECT rental_rate, MAX(rental_rate) FROM film
GROUP BY rental_rate

SELECT 
SUM(
	CASE
		WHEN rental_rate = 4.99 THEN 1
		ELSE 0
	END
) AS cate
FROM film