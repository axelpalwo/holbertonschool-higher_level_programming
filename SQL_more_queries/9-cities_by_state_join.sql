-- Select ID and Name from Cities and State_Name with () to resolve and then look for
-- Then we sort it
SELECT cities.id, cities.name, states.name AS name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
