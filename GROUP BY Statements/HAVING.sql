-- SELECT customer_id, SUM(amount) FROM payment
-- GROUP BY customer_id
-- HAVING customer_id NOT IN(123, 43, 144, 87) AND SUM(amount) > 100

-- • Challenge
-- 。 We are launching a platinum service for
-- our most loyal customers. We will assign
-- platinum status to customers that have
-- had 40 or more transaction payments.
-- 。 What customer_ids are eligible for
-- platinum status?

-- SELECT customer_id, COUNT(amount) FROM payment
-- GROUP BY customer_id
-- HAVING COUNT(amount) >= 40 

-- • Challenge
-- 。 What are the customer ids of customers
-- who have spent more than $100 in
-- payment transactions with our staff_id
-- member 2?

SELECT staff_id, customer_id, SUM(amount) FROM payment
GROUP BY staff_id, customer_id
HAVING SUM(amount) >= 100 AND staff_id = 2
ORDER BY SUM(amount) ASC