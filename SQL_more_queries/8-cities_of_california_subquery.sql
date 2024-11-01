-- Get the id of California from the states table and save it
-- We use the California id and pass it to Where in Cities
SET @california_id = (SELECT id FROM states WHERE name = 'California' LIMIT 1);

SELECT id, name FROM cities WHERE state_id = @california_id ORDER BY id ASC;
