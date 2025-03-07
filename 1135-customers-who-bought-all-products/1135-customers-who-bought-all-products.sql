# Write your MySQL query statement below
SELECT c.customer_id
from Customer c
join Product p
group by customer_id
having count(distinct c.product_key)=count(distinct p.product_key);