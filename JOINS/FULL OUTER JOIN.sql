SELECT * FROM payment
FULL OUTER JOIN customer
ON payment.customer_id = customer.customer_id
WHERE payment.customer_id IS null OR customer.customer_id IS null