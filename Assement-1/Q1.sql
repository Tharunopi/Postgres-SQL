-- Return the customer IDs of customers who have spent 
-- at least $110 with the staff member who has an ID of 2.

SELECT customer_id , SUM(amount) FROM payment
GROUP BY staff_id, customer_id
HAVING SUM(amount) >= 110 AND staff_id = 2