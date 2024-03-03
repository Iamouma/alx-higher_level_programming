-- This creates the table id_not_null on my MySQL server

-- creating table with an id default value of 1
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
