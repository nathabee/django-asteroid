--- these files are just informative and are not used
-- instead we create database object from manage.py and the django models
-- see file in games/models.py


-- Table to store user login information (using a standard package is assumed later, but here's a basic structure)
CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL UNIQUE,
       password_hash VARCHAR(255) NOT NULL,
       email VARCHAR(100),
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   -- Table to store information about space objects (e.g., asteroids, planets)
   CREATE TABLE space_objects (
       id INT AUTO_INCREMENT PRIMARY KEY,
       object_type ENUM('asteroid', 'planet') NOT NULL,
       pos_x FLOAT NOT NULL,
       pos_y FLOAT NOT NULL
   );

   -- Table to store information about rockets
   CREATE TABLE rockets (
       id INT AUTO_INCREMENT PRIMARY KEY,
       player_id INT NOT NULL,
       pos_x FLOAT NOT NULL,
       pos_y FLOAT NOT NULL,
       speed_x FLOAT NOT NULL,
       speed_y FLOAT NOT NULL,
       status ENUM('active', 'destroyed') DEFAULT 'active',
       FOREIGN KEY (player_id) REFERENCES players(id) ON DELETE CASCADE
   );

   -- Table to store player information and scores
   CREATE TABLE players (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL UNIQUE,
       score INT DEFAULT 0,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
