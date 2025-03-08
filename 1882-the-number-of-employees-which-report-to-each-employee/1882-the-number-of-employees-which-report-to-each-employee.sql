SELECT e1.employee_id,
e1.name,
count(e2.employee_id) as reports_count,
round(avg(e2.age))as average_age
FROM Employees e1
inner join Employees e2
on e1.employee_id=e2.reports_to
group by e1.employee_id,e1.name
order by employee_id;