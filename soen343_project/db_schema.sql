-- drop DATABASE if EXISTS test;
-- CREATE DATABASE test;
-- USE test;
CREATE TABLE users
(
	id INTEGER PRIMARY KEY AUTO_INCREMENT
);
CREATE TABLE roles
(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL
);
CREATE TABLE has_role
(
	user_id INTEGER NOT NULL REFERENCES users(id),
	role_id INTEGER NOT NULL REFERENCES roles(id)
);
CREATE TABLE auth
(
	user_id INTEGER NOT NULL REFERENCES users(id),
	password VARCHAR(255) NOT NULL
);
CREATE TABLE addresses
(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	civic_num INTEGER NOT NULL,
	street_name VARCHAR(255) NOT NULL,
	city VARCHAR(255) NOT NULL,
	state VARCHAR(255),
	country VARCHAR(255) NOT NULL
);
CREATE TABLE clients
(
	user_id INTEGER NOT NULL REFERENCES users(id),
	f_name VARCHAR(255) NOT NULL,
	l_name VARCHAR(255) NOT NULL,
	email  VARCHAR(255),
	address_id INTEGER REFERENCES addresses(id),
	phone_num INTEGER(11),
	loan_item_count INTEGER NOT NULL,
	CONSTRAINT clients1_max_items CHECK(loan_item_count <= 25) -- might need to come back to this limit, its arbitrary atm
);
CREATE TABLE items
(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	type VARCHAR(255) NOT NULL
);
CREATE TABLE item_properties
(
	item_id INTEGER NOT NULL REFERENCES item(id),
	property VARCHAR(255) NOT NULL,
	name VARCHAR(255) NOT NULL
);
CREATE TABLE catalog
(
	item_id INTEGER NOT NULL REFERENCES item(id),
	quantity INTEGER NOT NULL, 
	CONSTRAINT catalog1_valid_quantity CHECK(quantity >= 0),
	loan_duration INTEGER NOT NULL, -- this quantity needs some units, we should decide on this at some point (hours seem flexible)
	CONSTRAINT catalog2_valid_duration CHECK(loan_duration > 0)
);
CREATE TABLE loan_states
(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(255) NOT NULL
);
CREATE TABLE loans
(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
	client_id INTEGER NOT NULL REFERENCES clients(user_id),
	return_date TIMESTAMP NOT NULL,
	lent_date TIMESTAMP NOT NULL,
	state_id INTEGER NOT NULL REFERENCES loan_states(id)
);
CREATE TABLE loan_items
(
	loan_id INTEGER NOT NULL REFERENCES loans(id),
	item_id INTEGER NOT NULL REFERENCES items(id),
	quantity INTEGER NOT NULL,
    CONSTRAINT loan_items1_valid_quantity CHECK(quantity > 0)
);  
