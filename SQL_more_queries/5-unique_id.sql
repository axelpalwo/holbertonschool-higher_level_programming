-- Create a table
-- name of column - type of data - DEFAULT (Value) - Primary/Foreign Key (Optional) - constrictions (Optional)
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL
);
