-- SELECT staff_id, amount, SUM(amount) FROM payment
-- GROUP BY staff_id, amount
-- ORDER BY staff_id, amount

-- SELECT customer_id, SUM(amount) FROM payment
-- GROUP BY customer_id
-- ORDER BY SUM(amount) DESC

-- SELECT staff_id, customer_id, SUM(amount) FROM payment
-- GROUP BY staff_id, customer_id
-- ORDER BY staff_id ASC, customer_id

SELECT DATE(payment_date), SUM(amount) FROM payment
GROUP BY DATE(payment_date)
ORDER BY SUM(amount) DESC