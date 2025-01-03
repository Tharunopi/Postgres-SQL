CREATE TABLE billing(
	product_id SERIAL PRIMARY KEY,
	price INTEGER NOT NULL,
	discount INTEGER
)

SELECT * FROM billing

INSERT INTO billing(price, discount)
VALUES 
	(100, 20),
	(200, null),
	(300, 10)

SELECT *, (price - COALESCE(discount, 0)) AS final_price FROM billing 
