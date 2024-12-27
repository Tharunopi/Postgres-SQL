SELECT staff_id, SUM(amount), MIN(amount), MAX(amount), ROUND(AVG(amount), 2) FROM payment
GROUP BY staff_id