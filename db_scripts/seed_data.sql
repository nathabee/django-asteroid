-- Insert initial data into the `users` table 
--  the password is clearly  :-)  
--  from django.contrib.auth.hashers import make_password
--  # Password to hash
--  plain_password = ':-)'
--  hashed_password = make_password(plain_password)
--  print(hashed_password)

INSERT INTO users (username, password_hash, email) VALUES
('alice', 'pbkdf2_sha256$260000$G9Y5OTY2ZTg1$DXrK0fOd7zKTKTRvVWxhDOV5s5Ij2mUFSJLPJm6soWg=', 'alice@example.com'),
('bob', 'pbkdf2_sha256$260000$G9Y5OTY2ZTg1$DXrK0fOd7zKTKTRvVWxhDOV5s5Ij2mUFSJLPJm6soWg=', 'bob@example.com'),
('carol', 'pbkdf2_sha256$260000$G9Y5OTY2ZTg1$DXrK0fOd7zKTKTRvVWxhDOV5s5Ij2mUFSJLPJm6soWg=', 'carol@example.com');



-- Insert initial data into the `space_objects` table
INSERT INTO space_objects (object_type, pos_x, pos_y) VALUES
('asteroid', 10.5, 20.3),
('asteroid', 30.2, 40.1),
('planet', 50.5, 60.6);

-- Insert initial data into the `players` table
INSERT INTO players (username, score) VALUES
('alice', 1000),
('bob', 1500),
('carol', 2000);

-- Insert initial data into the `rockets` table
-- Note: The player_id should correspond to the ids in the `players` table
INSERT INTO rockets (player_id, pos_x, pos_y, speed_x, speed_y, status) VALUES
(1, 12.3, 23.4, 1.2, 2.3, 'active'),
(2, 34.5, 45.6, 2.1, 3.4, 'active'),
(3, 56.7, 67.8, 3.2, 4.5, 'destroyed');

