-- UNIONS

-- A union is how you can combine rows together
-- not columns like we have been doing with joins where one column is put to next each other
-- join allow you to combine the rows of data

-- Now you should keep it the same kind of data otherwise...
-- if you start mixing tips with first_name it would really confusing

-- Let's try it out and use Union to bring together some random data,
-- then we will look at an actual use case



-- Sometimes you can't just combine random data together
-- This is the bad example because you are mixing the data
SELECT first_name, last_name
FROM employee_demographic
UNION
SELECT occupation, salary
FROM employee_salary
;

-- notice it gets rid of duplicates? "Union" is actually shorthand for "Union Distinct"
SELECT first_name, last_name
FROM employee_demographic
UNION -- or UNION DISTINCT
SELECT first_name, last_name
FROM employeee_salary
;

-- USE "UNION ALL" to show all values
SELECT first_name, last_name
FROM employee_demographic
UNION ALL
SELECT first_name, last_name
FROM employee_salary
;

-- Excercise: 1
-- The Parks department is trying to cut their budget
-- wants to identify older employees they can push out 
-- or high paid employees who they can reduce pay or push out
-- let's create some queries to help with this

-- ANSWER:
SELECT first_name, last_name, 'Old Lady' AS Label -- identify as old lady
FROM employee_demographic
WHERE age > 55 AND gender = 'Female'

UNION

SELECT first_name, last_name, 'Old Gentlemen' AS Label -- identify as old gentlemen
FROM employee_demographic
WHERE age > 55 AND gender = 'Male'

UNION

SELECT first_name, last_name, 'Over Paid' AS Label -- identify as high paid
FROM employee_salary
WHERE salary >= 80000
ORDER BY frist_name, last_name
;