-- Create a table users with unique users and country
DROP TABLE IF EXISTS users;
CREATE TABLE users (

    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
