CREATE DATABASE corporate_projects;
USE corporate_projects;

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2),
    joining_date DATE
);

CREATE TABLE Projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(120) NOT NULL,
    start_date DATE,
    end_date DATE
);

CREATE TABLE Employee_Project (
    emp_id INT,
    project_id INT,
    hours_worked INT,
    rating DECIMAL(3,2),
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id)
);

INSERT INTO Employees (emp_name, department, salary, joining_date) VALUES
('Arvind Mehta','Data Science',82000,'2020-03-12'),
('Nisha Kapoor','Cyber Security',76000,'2019-11-21'),
('Devansh Kulkarni','Cloud Engineering',88000,'2021-07-09'),
('Tanvi Srivastava','AI Research',91000,'2018-05-30'),
('Raghav Menon','DevOps',73000,'2022-01-18'),
('Sakshi Bansal','Product Analytics',79000,'2020-10-06'),
('Kabir Narang','Cyber Security',70500,'2023-02-25');

INSERT INTO Projects (project_name,start_date,end_date) VALUES
('Autonomous Drone Navigation','2023-01-10','2023-07-20'),
('Blockchain Payment Gateway','2023-02-15','2023-09-10'),
('Smart City Traffic Prediction','2023-03-05','2023-11-18'),
('Healthcare Data Intelligence','2023-04-12','2023-10-30'),
('Retail Demand Forecasting','2023-05-08','2023-12-15');

INSERT INTO Employee_Project VALUES
(1,1,140,4.6),
(1,3,120,4.4),
(1,5,95,4.3),
(2,2,110,4.1),
(2,3,85,3.9),
(3,1,160,4.8),
(3,4,150,4.7),
(4,3,170,4.9),
(4,4,130,4.6),
(5,5,100,4.0),
(6,2,115,4.5),
(6,5,105,4.2);

SELECT e.emp_name
FROM Employees e
JOIN Employee_Project ep
ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.emp_name
HAVING COUNT(ep.project_id) > 2;

SELECT e.emp_name, AVG(ep.rating) AS avg_rating
FROM Employees e
JOIN Employee_Project ep
ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.emp_name
HAVING AVG(ep.rating) > 4;

SELECT emp_name, department, salary
FROM Employees e
WHERE salary = (
    SELECT MAX(salary)
    FROM Employees
    WHERE department = e.department
);

SELECT emp_name
FROM Employees
WHERE emp_id NOT IN (
    SELECT emp_id
    FROM Employee_Project
);

SELECT p.project_name, SUM(ep.hours_worked) AS total_hours
FROM Projects p
JOIN Employee_Project ep
ON p.project_id = ep.project_id
GROUP BY p.project_id, p.project_name
ORDER BY total_hours DESC
LIMIT 1;