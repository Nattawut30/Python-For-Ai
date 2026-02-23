-- Common Table Expressions (CTE)
-- allows you to define a subquery block that can be referenced within the main query
-- It is particularly useful for recursive queries or queries that require referencing a higher level
-- this is something we will look at in the next lesson

-- CTE start using a "WITH" keywords then name this CTE anything we want
-- Then we say as and within the parenthesis we build our subquery/table we want

WITH CTE_Example AS ( 
SELECT gender, AVG(salary) avg_sal, MAX(salary) max_sal, MIN(salary) min_sal, COUNT(salary) count_sal
FROM employee_demographic AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender
)
-- directly after using it we can query the CTE
SELECT *
FROM CTE_Example
;

-- Now we can use the columns within this CTE to do calculation on this data that
-- we couldn't have done without it

WITH CTE_Example AS
( 
SELECT gender, AVG(salary) avg_sal, MAX(salary) max_sal, MIN(salary) min_sal, COUNT(salary) count_sal
FROM employee_demographic AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender
)
SELECT gender, ROUND(AVG(SUM(salary)/COUNT(salary)),2)
FROM CTE_Example
;

-- we also have the ability to create multiple CTEs with just one With Expression

WITH CTE_Example AS
(
SELECT employee_id, gender, birth_date
FROM employee_demographic
WHERE birth_date > '2000-01-30'
),
CTE_Example_2 AS
(
SELECT employee_id, salary
FROM employee_salary
WHERE salary > 50000
)
SELECT *
FROM CTE_Example
JOIN CTE_Example_2
	ON CTE_Example.employee_id = CTE_Example_2.employee_id
;

-- the last thing I wanted to show you is that we can actually make our life easier by renaming the columns in the CTE
-- let's take our very first CTE we made. We had to use tick marks because of the column names

-- we can rename them like this

WITH CTE_Example (gender, sum_salary, min_salary, max_salary, count_salary) AS
(
SELECT gender, SUM(salary), MIN(salary), MAX(salary), COUNT(salary)
FROM employee_demographic AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender
)
-- notice here I have to use back ticks to specify the table names
-- without them it doesn't work
SELECT gender, ROUND(AVG(sum_salary/count_salary),2)
FROM CTE_Example
GROUP BY gender
;