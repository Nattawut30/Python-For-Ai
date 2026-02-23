-- SUBQUERIES

-- queries within queries.

-- Now let's say we wanted to look at employees who actually work in the Parks and Rec Department, 
-- we could join tables together or we could use a subquery
-- We can do that like this:

SELECT *
FROM employee_demographic
WHERE employee_id IN (
				SELECT employee_id
					FROM employee_salry
					WHERE dept_id = 1)
;

-- Using that subquery in the where statement and if we just highlight the subquery and run it
-- it basically, a list we are selecting from in the outer query

-- now if we try to have more than 1 column in the subquery we get an error 
-- saying the operand should contain 1 column only 

-- We can also use subqueries in the select and the from statements - let's see how we can do this
-- Let's say we want to look at the salaries and compare them to the average salary

-- it's giving us the average PER GROUP which we don't want
-- here's a good use for a subquery
SELECT frist_name, salary, 
						(SELECT AVG(salary)
							FROM employee_salary)
FROM employee_salary
GROUP BY first_name, salary
;
-- We can compare it really quickly just like that!


-- We can also use it in the FROM Statement
-- when we use it here it's almost like we are creating a small table 
-- we are querying off of
SELECT gender, AVG(age), MAX(age), MIN(age), COUNT(age)
FROM employee_demographic
GROUP BY gender
;
-- now this doesn't work because we get an error saying we have to name it

-- The correct version:
SELECT AVG(max_age)
FROM (
	SELECT gender,
    AVG(age) AS avg_age,
    MAX(age) AS max_age,
    MIN(age) AS min_age,
    COUNT(age)
		FROM employee_demographic
		GROUP BY gender)
AS age_table
;