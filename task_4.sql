-- Prints the full description of the table 'books' from the database 'alx_book_store'.
-- This script queries the information_schema.COLUMNS table, as DESCRIBE/EXPLAIN are forbidden.
-- All SQL keywords are in uppercase.

SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM
    information_schema.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store'
AND
    TABLE_NAME = 'books'
ORDER BY
    ORDINAL_POSITION;


