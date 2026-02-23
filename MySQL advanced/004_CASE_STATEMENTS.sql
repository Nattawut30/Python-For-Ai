-- Case Statements

-- Allows you to add logic to your select statements
-- sort of like an if else statement in other programming languages
-- or even things like Excel

SELECT fist_name, last_name, age,
CASE
	WHEN age <= 30 THEN 'Rookie'
    WHEN age BETWEEN 31 AND 50 THEN 'Experienced'
    WHEN age >= 51 THEN 'Veteran'
END AS age_bracket
FROM employee_demographic
;

-- Now we don't just have to do simple labels like we did, 
-- we can also perform calculations

-- Let's look at giving bonuses to employees

-- Pay Increase and Bonus
-- < 50000 = 5%
-- > 50000 = 7%
-- Finance = 10% bonus

SELECT first_name, last_name, salary,
CASE
	WHEN salary < 50000 THEN salary * 1.05
    WHEN salary > 50000 THEN salary * 1.07
END AS new_salary
FROM employee_salary;

-- Now we need to also account for Bonuses, let's make a new column

SELECT first_name, last_name, salary,
CASE
	WHEN salary < 50000 THEN salary * 1.05
    WHEN salary > 50000 THEN salary * 1.07
END AS new_salary,
CASE
	WHEN dept_id = 6 THEN salary * .10
END AS bonus
FROM employee_salary;

-- as you can see Ben is the only one who get's a bonus


