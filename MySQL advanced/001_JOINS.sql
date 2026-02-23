-- 1. JOINS

-- joins allow you to combine 2 tables together (or more) if they have a common column.
-- doesn't mean they need the same column name, but the data in it are the same and can be used to join the tables together
-- there are several joins we will look at today, inner joins, outer joins, and self joins


-- Check out this 2 tables
SELECT *
FROM employee_demographics;

SELECT *
FROM employee_salary;

-- JOIN & INNER JOIN return rows that are the same in both columns
-- we have the same columns so we need to specify which table they're coming from

SELECT *
FROM employee_demographics AS dem
INNER JOIN  employee_salary AS sal
	ON dem.employee_id = sal.employee_id
; 
-- USE . or dot to specify so it's not ambiguous
-- use aliasing! It's easier to read.


-- more specify version
SELECT dem.employee_id, age, occupation
FROM employee_demographic AS dem
INNER JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
;

-- 2. OUTER JOIN

-- for outer joins we have a left and a right join
-- a left join will take everything from the left table even no match in the join,
-- but will only return matches from the right table
-- the exact opposite is true for a right join

SELECT *
FROM employee_demographic AS dem
LEFT OUTER JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
;

-- so you'll notice we have everything from the left table or the salary table. Even though no Ron Swans
-- Since there is not match on the right table it's just all Nulls

-- if we just switch this to a right join it basically just looks like an inner join

SELECT *
FROM employee_demographic AS dem
RIGHT JOIN employee_salary as sal
	ON dem.employee_id = sal.employee_id
;

-- 3. SELF JOIN
-- a self join is where you tie a table to itself

-- now let's change it to give them their secret santa
SELECT *
FROM employee_salary emp1
JOIN employee_salary emp2
	ON emp1.employee_id + 1 = emp2.employee_id
;

-- Customize more on the table

SELECT emp1.employee_id AS emp_santa,
emp1.first_name AS first_name_santa, 
emp1.last_name AS last_name_santa,
emp2.employee_id AS emp_name,
emp2.first_name AS first_name_emp,
emp2.last_name AS last_name_emp
FROM employee_salary emp1
JOIN employee_salary emp2
	ON emp1.employee_id + 1 = emp2.employee_id
;

-- 4. Joining Multiple Tables Together

-- Reference tables we have on other table we can join
SELECT *
FROM parks_departments;

-- Tie em' up together with the ref. that never change!
SELECT *
FROM employee_demographic AS dem
INNER JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
JOIN parks_departments pd
	ON sal.dept_id = pd.department_id
;

-- now notice when we did that, since it's an inner join it got rid of andy because he wasn't a part of any department

-- if we do a left join we would still include him because we are taking everything from the left table
-- which is the salary table in this instance
SELECT *
FROM employee_demographics dem
INNER JOIN employee_salary sal
	ON dem.employee_id = sal.employee_id
LEFT JOIN parks_departments pd
	ON pd.department_id = sal.dept_id;