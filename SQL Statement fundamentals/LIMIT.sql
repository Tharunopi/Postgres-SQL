-- SELECT * FROM payment
-- WHERE amount != 0 
-- ORDER BY payment_date
-- LIMIT 10;

-- Challenge Task
-- 。 We want to reward our first 10 paying
-- customers.
-- 。 What are the customer ids of the first 10
-- customers who created a payment?

-- SELECT customer_id FROM payment
-- ORDER BY payment_date ASC
-- LIMIT 10;

-- Challenge Task
-- 。 A customer wants to quickly rent a
-- video to watch over their short lunch
-- break.
-- 。 What are the titles of the 5 shortest (in
-- length of runtime) movies?

SELECT title, length FROM film
ORDER BY length ASC
LIMIT 5;