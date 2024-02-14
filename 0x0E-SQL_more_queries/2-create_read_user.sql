-- This script creates the database hbtn_0d_2 and user user_0d_2

-- Creating database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- creating user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
FLUSH PRIVILEGES;

-- granting permission to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
