CREATE DATABASE employee_performance;
USE employee_performance;

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO Employees (emp_name, department, salary) VALUES
('Vikram Nair','Data Engineering',85000),
('Ananya Ghosh','AI Research',92000),
('Siddharth Jain','Cloud Infrastructure',78000),
('Pooja Verma','AI Research',88000),
('Harsh Agarwal','Cyber Security',81000),
('Neha Kulkarni','Data Engineering',76000),
('Rohan Bhatt','Cyber Security',95000),
('Ishita Chatterjee','Cloud Infrastructure',83000),
('Aditya Sharma','AI Research',99000),
('Kunal Mehta','Data Engineering',72000);

SELECT emp_name, salary
FROM Employees
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
);

SELECT e.emp_name, e.department, e.salary
FROM Employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM Employees
    WHERE department = e.department
);

SELECT emp_name, department, salary
FROM Employees e
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees
    WHERE department = e.department
);

SELECT emp_name, salary
FROM Employees
WHERE salary < (
    SELECT MAX(salary)
    FROM Employees
)
AND salary > (
    SELECT AVG(salary)
    FROM Employees
);

SELECT department, AVG(salary) AS dept_avg_salary
FROM Employees
GROUP BY department
HAVING AVG(salary) > (
    SELECT AVG(salary)
    FROM Employees
);