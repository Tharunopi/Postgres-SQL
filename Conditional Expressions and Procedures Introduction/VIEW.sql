CREATE VIEW customer_address AS
SELECT first_name, last_name, address FROM customer
INNER JOIN address
ON address.address_id = customer.address_id

SELECT * FROM customer_address

CREATE OR REPLACE VIEW customer_address AS
SELECT first_name, last_name, address, district FROM customer
INNER JOIN address
ON address.address_id = customer.address_id

DROP VIEW IF EXISTS customer_address

ALTER VIEW customer_address
TO c_add