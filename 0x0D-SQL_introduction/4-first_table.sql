-- creates a table first_table in current database in my MySQL server.
-- does not fail if table exists
CREATE TABLE IF NOT EXISTS first_table (id INT,
name VARCHAR(256));
