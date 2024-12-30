-- TIME contains only time
-- DATE contains only date
-- TIMESTAMP contains both date and time
-- TIMESTAMPTZ contains date, time, and timezone

-- SHOW TIMEZONE
-- SELECT TIMEOFDAY()

-- SELECT EXTRACT(YEAR FROM last_update), EXTRACT(MONTH FROM last_update) FROM customer
-- SELECT AGE(last_update) FROM customer
-- SELECT AGE(payment_date) AS how_old FROM payment
-- ORDER BY AGE(payment_date) DESC

SELECT TO_CHAR(payment_date, 'HH12:MI:SS  (MON-YYYY)') FROM payment 