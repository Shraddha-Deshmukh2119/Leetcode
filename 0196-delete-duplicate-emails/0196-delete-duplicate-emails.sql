DELETE p1
FROM Person p1 INNER JOIN Person p2
Where p1.email=p2.email and p1.id > p2.id