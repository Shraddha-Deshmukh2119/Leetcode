# Write your MySQL query statement below
SElect w1.id
from weather w1
inner join weather  w2
where DATEDIFF(w1.recordDate,w2.recordDate)=1
AND w1.temperature >w2.temperature;