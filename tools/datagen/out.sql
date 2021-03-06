DROP DATABASE homework;
CREATE DATABASE homework CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE homework;
CREATE TABLE students(
	student_uid INT,
	name VARCHAR(255),
	address VARCHAR(255),
	tel INT,
	email VARCHAR(255),
	date_birth DATETIME,
	gender VARCHAR(255),
	category VARCHAR(255),
	special_needs VARCHAR(255),
	comment VARCHAR(255),
	status VARCHAR(255),
	school VARCHAR(255),
	department VARCHAR(255)
);
CREATE TABLE halls(
	name VARCHAR(255),
	tel INT,
	staff_number INT,
	place_number INT
);
CREATE TABLE rooms(
	place_number INT,
	room_number INT,
	rent INT,
	address VARCHAR(255)
);
CREATE TABLE flats(
	apt_number INT,
	number_rooms INT,
	place_number INT
);
CREATE TABLE leases(
	lease_number INT,
	duration INT,
	student_name VARCHAR(255),
	student_uid INT,
	place_number INT,
	moving_in DATETIME,
	moving_out DATETIME
);
CREATE TABLE invoices(
	invoice_number INT,
	lease_number INT,
	payment_due DATETIME,
	student_uid INT,
	place_number INT,
	paid DATETIME,
	method VARCHAR(255),
	first_reminder DATETIME,
	second_reminder DATETIME
);
CREATE TABLE inspections(
	staff_number INT,
	name VARCHAR(255),
	inspected VARCHAR(255),
	satisfactory VARCHAR(255),
	comments VARCHAR(255)
);
CREATE TABLE staff(
	staff_number INT,
	name VARCHAR(255),
	email INT,
	address VARCHAR(255),
	date_birth DATETIME,
	position VARCHAR(255),
	location VARCHAR(255),
	tel INT
);
CREATE TABLE Next-of-kin(
	student_uid INT,
	name VARCHAR(255),
	relation VARCHAR(255),
	address VARCHAR(255),
	tel INT
);
