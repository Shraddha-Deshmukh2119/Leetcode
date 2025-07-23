# Write your MySQL query statement below
SELECT *
FROM Patients
where
conditions like ('DIAB1%') OR conditions like ('% DIAB1%')
