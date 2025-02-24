# Write your MySQL query statement below
select p.product_id,ifnull(round(sum(p.price*s.units)/SUM(s.units),2),0) as average_price
from Prices p
Left join UnitsSold s
ON p.product_id=s.product_id
And s.purchase_date>=p.start_date And s.purchase_date <=p.end_date
group by p.product_id;