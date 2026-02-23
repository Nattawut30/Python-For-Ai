-- WINDOW FUNCTION

-- somewhat like a group by BUT don't roll everything up into 1 row when grouping
-- allow us to look at a partition or a group,
-- but they each keep their own unique rows in the output
-- Let's look at things like Row Numbers, Rank, and Dense Rank
-- OVER()

-- First Let's take a look at group by
SELECT gender, AVG(salary) AS avg_salary
FROM employee_demographic AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
GROUP BY gender;

-- NOW let's try doing something similar  with window function
SELECT gender, AVG(salary) OVER(PARTITION BY gender) -- use this
FROM employee_demographic AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
;

-- now we can add any columns and it works, 
-- We could get this exact same output with a subquery in the select statement, 
-- but window functions have a lot more functionality, let's take a look.

-- if we use partition it's kind of like the group by except it doesn't roll up - 
-- it just partitions or breaks based on a column when doing the calculation
SELECT dem.first_name, dem.last_name, gender,
AVG(salary) OVER(PARTITION BY gender)
FROM employee_demographic AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
;

-- Now if we wanted to see what the salaries were for genders we could do that
-- by using sum, but also we could use order by to get a rolling total
SELECT dem.employee_id, dem.first_name, gender, salary,
SUM(salary) OVER(PARTITION BY gender ORDER BY employee_id) AS rolling_total
FROM employee_demographic AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
;

-- Let's look at row_number rank and dense rank now
-- and try ordering by salary so we can see the order of highest paid employees by gender
SELECT dem.employee_id, dem.first_name, gender, salary,
ROW_NUMBER() OVER(PARTITION BY gender ORDER BY salary DESC)
FROM employee_demographic AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
;

-- Compare this to rank
SELECT dem.employee_id, dem.first_name, gender, salary,
ROW_NUMBER() OVER(PARTITION BY gender ORDER BY salary DESC) AS row_num,
Rank() OVER(PARTITION BY gender ORDER BY salary DESC) AS rank_num
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
;
-- notice rank repeats on tom & jerry at 5, but then skips 6 to go to 7 
-- this goes based off positional rank

-- Compare this to dense rank
SELECT dem.employee_id, dem.first_name, gender, salary,
ROW_NUMBER() OVER(PARTITION BY gender ORDER BY salary DESC) AS row_num,
Rank() OVER(PARTITION BY gender ORDER BY salary DESC) AS rank_num,
DENSE_RANK() OVER(PARTITION BY gender ORDER BY salary DESC) AS dense_rank_num
FROM employee_demographics AS dem
JOIN employee_salary AS sal
	ON dem.employee_id = sal.employee_id
;