-- script 100
-- converts hbtn_0c_0 database to UTF8(utf8mb4, collate utf8mb4_unicode_ci) 
-- in your MySQL server

/* Convert the hbtn_0c_0 database to UTF-8 */
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

/* Convert the first_table to UTF-8 */
ALTER TABLE hbtn_0c_0.first_table 
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

/* Convert the name field in the first_table to UTF-8 */
ALTER TABLE hbtn_0c_0.first_table
MODIFY COLUMN name VARCHAR(256)
CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
