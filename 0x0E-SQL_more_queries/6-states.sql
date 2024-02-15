-- creates a db and table
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE states(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);