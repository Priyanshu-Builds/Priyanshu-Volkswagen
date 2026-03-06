CREATE DATABASE ecommerce_analysis;
USE ecommerce_analysis;

CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    quantity INT,
    total_amount DECIMAL(10,2)
);

INSERT INTO Orders (customer_id, product_id, quantity, total_amount) VALUES
(101, 1, 25, 12500),
(101, 2, 30, 12000),
(101, 3, 18, 7200),
(101, 4, 22, 8800),

(102, 2, 35, 14000),
(102, 3, 17, 6800),

(103, 1, 40, 16000),
(103, 4, 30, 12000),
(103, 5, 16, 6400),

(104, 3, 25, 10000),
(104, 2, 22, 8800),
(104, 1, 19, 7600),
(104, 5, 15, 6000),

(105, 4, 50, 20000),
(105, 2, 20, 8000),

(106, 5, 13, 5200);

SELECT customer_id, SUM(total_amount) AS total_spent
FROM Orders
GROUP BY customer_id;

SELECT customer_id, COUNT(order_id) AS total_orders
FROM Orders
GROUP BY customer_id;

SELECT customer_id, COUNT(order_id) AS order_count
FROM Orders
GROUP BY customer_id
HAVING COUNT(order_id) > 3;

SELECT customer_id, SUM(total_amount) AS total_spending
FROM Orders
GROUP BY customer_id
HAVING SUM(total_amount) > 10000;

SELECT product_id, SUM(quantity) AS total_quantity_sold
FROM Orders
GROUP BY product_id
HAVING SUM(quantity) > 100;