-- Table creation and sample data
CREATE TABLE IF NOT EXISTS Person (Id INT, Email VARCHAR(255));

INSERT INTO Person (id, email) VALUES ('1', 'john@example.com');
INSERT INTO Person (id, email) VALUES ('2', 'bob@example.com');
INSERT INTO Person (id, email) VALUES ('3', 'john@example.com');

TRUNCATE TABLE Person;

-- Solution query
DELETE p1
FROM Person p1
JOIN Person p2 ON p1.email = p2.email AND p1.id > p2.id;
