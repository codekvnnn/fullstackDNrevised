INSERT INTO dojos (name, created_at, updated_at) 
VALUES
--  SELECT * FROM dojos; -- TESTING EACH LINE**
('Dojo A', NOW(), NOW()),
('Dojo B', NOW(), NOW()),
('Dojo C', NOW(), NOW());
DELETE FROM dojos WHERE name IN ('Dojo A', 'Dojo B', 'Dojo C');
--  SELECT * FROM dojos; -- TESTING EACH LINE**
INSERT INTO dojos (name, created_at, updated_at) 
VALUES
--  SELECT * FROM dojos; -- TESTING EACH LINE**
('Dojo D', NOW(), NOW()),
('Dojo E', NOW(), NOW()),
('Dojo F', NOW(), NOW());
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
 VALUES
 --  SELECT * FROM dojos; -- TESTING EACH LINE**
('Ninja 1', 'A', 20, NOW(), NOW(), 1),
('Ninja 2', 'A', 21, NOW(), NOW(), 1),
('Ninja 3', 'A', 22, NOW(), NOW(), 1);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id)
 VALUES
--  SELECT * FROM dojos; -- TESTING EACH LINE**
 
('Ninja 4', 'B', 23, NOW(), NOW(), 2),
('Ninja 5', 'B', 24, NOW(), NOW(), 2),
('Ninja 6', 'B', 25, NOW(), NOW(), 2);
INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) 
VALUES
--  SELECT * FROM dojos; -- TESTING EACH LINE**
('Ninja 7', 'C', 26, NOW(), NOW );
SELECT * FROM dojos; -- TESTING EACH LINE**
--  SELECT * FROM dojos; -- TESTING EACH LINE**
SELECT * FROM ninjas WHERE dojo_id = 1; -- --Retrieve all the ninjas from the first dojo: 
--  SELECT * FROM dojos; -- TESTING EACH LINE**
SELECT * FROM ninjas WHERE dojo_id = (SELECT MAX(id) FROM dojos);-- Retrieve all the ninjas from the last dojo:
--  SELECT * FROM dojos; -- TESTING EACH LINE**
SELECT dojos.* FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id -- Retrieve the last ninja's dojo:
--  SELECT * FROM dojos; -- TESTING EACH LINE**
