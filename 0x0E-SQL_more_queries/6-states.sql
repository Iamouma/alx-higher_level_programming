-- This script creates the database hbtn_0d_usa
-- It also creates table states on my MySQL server

-- creating the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- use database created
USE hbtn_0d_usa;

-- creating the table id as the primary key
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT,
	name VARCHAR(256),
	PRIMARY KEY (id)
);
