# Write your MySQL query statement below
select e.name,b.bonus
from Employee e
left join Bonus b
On e.empId=b.empId
Where b.bonus is null or b.bonus<1000;