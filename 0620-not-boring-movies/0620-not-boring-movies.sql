# Write your MySQL query statement below
select c.id,c.movie,c.description,c.rating
from Cinema c
where c.id%2!=0 And c.description !='boring'
order by c.rating desc;