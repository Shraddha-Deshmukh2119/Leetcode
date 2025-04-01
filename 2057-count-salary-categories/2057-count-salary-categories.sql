select "Low Salary" as category,count(income)as accounts_count
from Accounts
where income <20000
union
select "Average Salary" as category,count(income)as accounts_count
from Accounts
where income >=20000 And income <=50000
union
select "High Salary" as category,count(income)as accounts_count
from Accounts
where income >50000