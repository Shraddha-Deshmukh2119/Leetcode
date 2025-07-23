-- SELECT 
--     (SELECT DISTINCT salary 
--      FROM Employee 
--      ORDER BY salary DESC 
--      LIMIT 1 OFFSET 1) AS SecondHighestSalary;

SELECT MAX(e1.salary) AS SecondHighestSalary
FROM Employee e1 INNER JOIN Employee e2
on e1.salary <e2.salary