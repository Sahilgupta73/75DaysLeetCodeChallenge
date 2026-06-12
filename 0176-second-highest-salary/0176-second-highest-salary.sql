# Write your MySQL query statement below
-- select salary AS SecondHighestSalary
-- from Employee
-- Limit 1 offset 1 

SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC 
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary