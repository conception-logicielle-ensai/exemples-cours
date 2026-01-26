CREATE SCHEMA demo;

CREATE TABLE demo.users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    country TEXT,
    age INTEGER
);

INSERT INTO demo.users (name, country, age)
SELECT
    'user_' || i,
    CASE
        WHEN i % 3 = 0 THEN 'FR'
        WHEN i % 3 = 1 THEN 'US'
        ELSE 'DE'
    END,
    18 + (i % 50)
FROM generate_series(1, 100) AS s(i);
