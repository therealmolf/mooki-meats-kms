CREATE DATABASE mooki_db;

#team_delete_ind bool
CREATE TABLE team (
	team_name VARCHAR(25) PRIMARY KEY,
	team_desc TEXT NOT NULL
);

CREATE TABLE emp (
	emp_id SERIAL PRIMARY KEY,
	emp_name VARCHAR(255) NOT NULL,
	team_name VARCHAR(25) REFERENCES team(team_name), 
	role_name VARCHAR(25) NOT NULL,
	ssn VARCHAR(11) NOT NULL,
	degree VARCHAR(255),
	emp_desc TEXT,
	date_hired DATE
	);

CREATE TABLE knowledge (
	know_id SERIAL PRIMARY KEY,
	know_type VARCHAR(30) NOT NULL,
	know_name VARCHAR(255) NOT NULL,
	know_desc TEXT NOT NULL,
	prop_date TIMESTAMP,
	prop_by VARCHAR(255),
	app_status VARCHAR(13)
	);

CREATE TABLE emp_know (
	emp_id SERIAL REFERENCES emp(emp_id),
	know_id SERIAL REFERENCES knowledge(know_id)
);

# Replication
# Step 1: Use psql or pgAdmin to create database above

# Step 2: Use populate_db.py to populate the database
# This should include two extra csv files called emp_sheet and know_sheet

# Step 3: Alter the tables to add delete_ind BOOLs
# ALTER TABLE emp ADD emp_delete_ind BOOL;
# ALTER TABLE knowledge ADD know_delete_ind BOOL;
# ALTER TABLE emp_know ADD emp_know_delete_ind BOOL;
