USE homework;

TRUNCATE TABLE flats;
TRUNCATE TABLE halls;
TRUNCATE TABLE inspections;
TRUNCATE TABLE invoices;
TRUNCATE TABLE leases;
TRUNCATE TABLE next_of_kin;
TRUNCATE TABLE rooms;
TRUNCATE TABLE staff;
TRUNCATE TABLE students;

LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables2/flats2.csv' INTO TABLE flats FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables2/halls2.csv' INTO TABLE halls FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables2/inspections2.csv' INTO TABLE inspections FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables2/invoices2.csv' INTO TABLE invoices FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables2/leases2.csv' INTO TABLE leases FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables2/Next-of-kin2.csv' INTO TABLE next_of_kin FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables2/rooms2.csv' INTO TABLE rooms FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables2/staff2.csv' INTO TABLE staff FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables2/students2.csv' INTO TABLE students FIELDS TERMINATED BY ';' LINES STARTING BY '';

/*
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables/flats.csv' INTO TABLE flats FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables/halls.csv' INTO TABLE halls FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables/inspections.csv' INTO TABLE inspections FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables/invoices.csv' INTO TABLE invoices FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables/leases.csv' INTO TABLE leases FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables/Next-of-kin.csv' INTO TABLE next_of_kin FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables/rooms.csv' INTO TABLE rooms FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables/staff.csv' INTO TABLE staff FIELDS TERMINATED BY ';' LINES STARTING BY '';
LOAD DATA LOCAL INFILE '/Users/simon/Docs/olandr/detamata/tools/datagen/tables/students.csv' INTO TABLE students FIELDS TERMINATED BY ';' LINES STARTING BY '';
*/
