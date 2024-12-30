-- SELECT payment.customer_id, customer.email, amount FROM payment
-- INNER JOIN customer
-- ON payment.customer_id = customer.customer_id
-- WHERE amount > (SELECT AVG(amount) FROM payment)

SELECT * FROM customer
WHERE activebool = true