-- Drop all rows in states and insert new
USE hbnb_dev_db;

DELETE FROM `states`;

INSERT INTO `states` VALUES 
    ('A','421a55f4-7d82-47d9-b51c-a76916479545','2016-03-25 19:42:40','2016-03-25 19:42:40'),
    ('B','421a55f4-7d82-47d9-b51c-a76916479546','2016-03-25 19:42:40','2016-03-25 19:42:40'),
    ('C','421a55f4-7d82-47d9-b52c-a76916479547','2016-03-25 19:42:40','2016-03-25 19:42:40'),
    ('D','421a55f4-7d82-47d9-b53c-a76916479548','2016-03-25 19:42:40','2016-03-25 19:42:40'),
    ('E','421a55f4-7d82-47d9-b57c-a76916479549','2016-03-25 19:42:40','2016-03-25 19:42:40');
