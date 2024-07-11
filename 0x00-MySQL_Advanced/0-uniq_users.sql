<<<<<<< HEAD
-- Task : 0. We are all unique! - creates a table users
-- script can be executed on any database
CREATE TABLE If NOT EXISTS `users` (  
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255)
=======
-- Creates a table with unique users.
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
>>>>>>> 5bdbc45c2096f3f83ddb7742e4cd518e147bb015
);
