CREATE DATABASE retail_analysis;
USE retail_analysis;

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    city VARCHAR(50)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(120),
    price DECIMAL(10,2)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Order_Items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

INSERT INTO Customers (name, city) VALUES
('Aditya Rao','Hyderabad'),
('Meera Iyer','Chennai'),
('Karan Malhotra','Delhi'),
('Simran Kaur','Amritsar'),
('Nikhil Deshpande','Pune'),
('Riya Shah','Ahmedabad'),
('Arjun Reddy','Bangalore');

INSERT INTO Products (product_name, price) VALUES
('Wireless Earbuds',2999),
('Gaming Keyboard',4599),
('Smart Fitness Band',1999),
('Bluetooth Speaker',3499),
('Portable SSD 1TB',7999),
('Laptop Cooling Pad',1299);

INSERT INTO Orders (customer_id, order_date, total_amount) VALUES
(1,'2024-01-10',4599),
(1,'2024-02-12',2999),
(1,'2024-03-05',1999),
(1,'2024-03-25',3499),
(2,'2024-01-18',7999),
(2,'2024-02-22',2999),
(3,'2024-01-11',1299),
(3,'2024-02-05',1999),
(4,'2024-02-17',3499),
(5,'2024-03-12',4599),
(6,'2024-03-20',2999);

INSERT INTO Order_Items (order_id, product_id, quantity) VALUES
(1,2,1),
(2,1,1),
(3,3,1),
(4,4,1),
(5,5,1),
(6,1,1),
(7,6,1),
(8,3,1),
(9,4,1),
(10,2,1),
(11,1,1);

SELECT c.name, COUNT(o.order_id) AS total_orders
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) > 3;

SELECT c.name, SUM(o.total_amount) AS total_spending
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spending DESC
LIMIT 5;

SELECT p.product_name, SUM(oi.quantity) AS total_ordered
FROM Products p
JOIN Order_Items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_ordered DESC
LIMIT 1;

SELECT name
FROM Customers
WHERE customer_id NOT IN (
    SELECT customer_id FROM Orders
);

SELECT DATE_FORMAT(order_date,'%Y-%m') AS month,
SUM(total_amount) AS monthly_revenue
FROM Orders
GROUP BY month
ORDER BY month;