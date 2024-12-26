-- SELECT * FROM payment
-- WHERE amount BETWEEN 8 AND 9
-- ORDER BY amount ASC;

SELECT * FROM payment
WHERE payment_date BETWEEN '2007-02-01' AND '2007-02-27'
ORDER BY payment_date ASC;