-- This script creates the table `force_name` on a MySQL server
--      id INT
--      name VARCHAR(256) can’t be null
CREATE TABLE IF NOT EXISTS `force_name`(
    id INT,
    name VARCHAR(256) NOT NULL
);
