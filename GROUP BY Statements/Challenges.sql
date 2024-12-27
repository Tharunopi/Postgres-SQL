-- SELECT staff_id, COUNT(amount) FROM payment
-- GROUP BY staff_id
-- ORDER BY COUNT(amount) DESC

-- • Corporate HQ is conducting a study on the
-- relationship between replacement cost
-- and a movie MPAA rating (e.g. G, PG, R,
-- etc...).
-- • What is the average replacement cost per
-- MPAA rating?
-- 。 Note: You may need to expand the AVG
-- column to view correct results

-- SELECT rating, ROUND(AVG(replacement_cost),2) FROM film
-- GROUP BY rating

-- • We are running a promotion to reward our
-- top 5 customers with coupons.
-- • What are the customer ids of the top 5
-- customers by total spend?

SELECT customer_id, SUM(amount) FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC
LIMIT 5