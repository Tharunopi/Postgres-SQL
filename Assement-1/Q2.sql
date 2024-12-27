-- 2. How many films begin with the letter J?

SELECT COUNT(*) FROM film
WHERE title LIKE 'J%'