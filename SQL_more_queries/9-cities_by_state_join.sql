-- Select ID and Name from Cities and State_Name with () to resolve and then look for
-- Then we sort it
SELECT cities.id, cities.name, 
       (SELECT name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
