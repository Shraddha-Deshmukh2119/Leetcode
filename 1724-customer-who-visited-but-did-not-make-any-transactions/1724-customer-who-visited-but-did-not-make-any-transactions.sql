# Write your MySQL query statement below
SElECT v.customer_id,count(customer_id) as count_no_trans
FROM Visits as v
Left Join Transactions as t
ON v.visit_id=t.visit_id
where t.transaction_id is null
Group by v.customer_id;