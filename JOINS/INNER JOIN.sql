SELECT payment_id, customer.customer_id, first_name FROM payment
INNER JOIN customer 
ON payment.customer_id = customer.customer_id