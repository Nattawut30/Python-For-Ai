-- STRING FUNCTION

-- These help us change and look at string differently.

SELECT *
FROM bakery.customers;

-- 1. Length: give us the length of each value
SELECT LENGTH('sky');

-- see the length of each name
SELECT first_name, LENGTH(fist_name)
FROM employee_demographic
ORDER BY 2;

-- 2. UPPER: will change all the string to upper case
SELECT UPPER('sky');

SELECT first_name, UPPER(fist_name)
FROM employee_demographic
;

-- 3.LOWER: will change all the string to upper case
SELECT LOWER('sky');

SELECT first_name, LOWER(first_name)
FROM employee_demographic
;

-- 4. TRIM: if you have values that have white space on the front or the end,
-- we can get rid of that white space using TRIM

SELECT TRIM('sky'     );

-- Now if we have white space in the middle it doesn't work
SELECT LTRIM('     I           love          SQL');

-- There's also L trim for trimming just the left side
SELECT LTRIM('     I love SQL');

-- There's also R trim for trimming just the Right side
SELECT RTRIM('I love SQL    ');

-- 5. LEFT: allow us to take amount of string from the left hand side
SELECT LEFT('Alexander', 4);

SELECT first_name, LEFT(first_name, 4)
FROM employee_demographic;

-- RIGHT: opposite, taking it starting from the right side
SELECT RIGHT('Alexander', 6);

SELECT first_name, RIGHT(first_name, 4)
FROM employee_demographic;

-- 6. SUBSTRING: allows you to specify a starting point and how many characters you want
-- so you can take characters from anywhere in the string. 
SELECT SUBSTRING('Alexander', 2, 3);

-- We could use this on phones to get the area code at the beginning
SELECT birth_date, SUBSTRING(birth_date, 1, 4) AS birth_year
FROM employee_dempgraphic;

-- 7. REPLACE
SELECT REPLACE(first_name, 'a', 'z')
FROM employee_demographic;

-- 8. LOCATE: We have 2 arguments we can use here
-- we can specify what we are searching for and where to search
-- It will return the position of that chatacter in the string
SELECT LOCATE('x', 'Alexander');

-- Alexcander has 2 'e' - what will happen if we try to locate it
SELECT LOCATE('e', 'Alexander');
-- It will return the location of just the first position.

-- try it on our first_name
SELECT first_name, LOCATE('a', first_name)
FROM employee_demographic;

-- You can also locate longer strings
SELECT first_name, LOCATE('Mic', first_name)
FROM employee_demographic;
; 
-- 9. CONCAT: concatenate, it will combine the string together
SELECT CONCAT('Leon', 'Kenedy');

-- Combine the first and last name columns together
SELECT fist_name, last_name, CONCAT(fist_name, ' ', last_name) AS full_name
FROM employee_demographic;