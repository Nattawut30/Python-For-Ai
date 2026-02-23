-- Stored Procedures

SELECT *
FROM employee_salary
WHERE salary >= 60000
;

-- Now let's put this into a stored procedure.
CREATE PROCEDURE large_salaries()
SELECT *
FROM employee_salary
WHERE salary >= 60000
;

-- Now if you run this it will work and create the stored procedure
-- we can click refresh and see that it is there

-- if we want to call it and use it we can call it by saying:
CALL large_salaries();
-- as you can see it ran the query inside the stored procedure we created

-- if we tried to add another query to this stored procedure it won't work
CREATE PROCEDURE large_salaries2()
SELECT *
FROM employee_salary
WHERE salary >= 60000;
SELECT *
FROM employee_salary
WHERE salary >= 50000
;
-- use delimiter and a Begin and End to really control what's in the stored procedure
-- let's see how we can do this
-- the delimiter is what seperates the queries by default,
-- we can change this to something like 2 $$

DELIMITER $$
CREATE PROCEDURE large_salaries2()
BEGIN
	SELECT *
	FROM employee_salary
	WHERE salary >= 60000;
	SELECT *
	FROM employee_salary
	WHERE salary >= 50000;
END $$
-- now we change the delimiter back after we use it to make it default again
DELIMITER $$ ;

-- it's going to drop the procedure if it already exists.
USE `parks_and_recreation`;
DROP PROCEDURE IF EXISTS `large_salaries3`;
-- it automatically adds the dilimiter for us

DELIMITER $$
CREATE PROCEDURE large_salaries3()
BEGIN
	SELECT *
	FROM employee_salary
	WHERE salary >= 60000;
	SELECT *
	FROM employee_salary
	WHERE salary >= 50000;
END $$

DELIMITER ;

-- and changes it back at the end

-- this can be a genuinely good option to help you write your Stored Procedures faster, although either way
-- works

-- if we click finish you can see it is created the same and if we run it

CALL large_order_totals3();
-- get our results

-- we can also add parameters
USE `parks_and_recreation`;
DROP procedure IF EXISTS `large_salaries3`;
-- it automatically adds the dilimiter for us
DELIMITER $$
CREATE PROCEDURE large_salaries4(employee_id_param INT)
BEGIN
	SELECT *
    FROM employee_salary
    WHERE salary >= 60000
    AND employee_id_param = employee_id;
END $$

DELIMITER ;

CALL large_salaries4(1);