-- Table creation and sample data
CREATE TABLE IF NOT EXISTS Employee (id INT, name VARCHAR(255), salary INT, managerId INT);

INSERT INTO Employee (id, name, salary, managerId) VALUES ('1', 'Joe', '70000', '3');
INSERT INTO Employee (id, name, salary, managerId) VALUES ('2', 'Henry', '80000', '4');
INSERT INTO Employee (id, name, salary, managerId) VALUES ('3', 'Sam', '60000', NULL);
INSERT INTO Employee (id, name, salary, managerId) VALUES ('4', 'Max', '90000', NULL);

TRUNCATE TABLE Employee;

-- Solution query
SELECT e1.name AS Employee
FROM Employee e1
JOIN Employee e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;
