# Write your MySQL query statement below
SELECT p.product_name,s.year,s.price
from Product as p
Right join Sales as s
On p.product_id=s.product_id;