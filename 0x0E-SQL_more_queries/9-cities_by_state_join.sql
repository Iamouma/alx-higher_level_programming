-- This script list all cities contained in the database

-- Use of join to display specific data
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
ON cities.states_id = states.id;
