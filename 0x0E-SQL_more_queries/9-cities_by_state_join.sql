-- This script lists all cities contained in the database `hbtn_0d_usa`
SELECT cities.id, cities.name, states.name
FROM cities
    NATURAL JOIN states
    ORDER BY cities.id ASC;
