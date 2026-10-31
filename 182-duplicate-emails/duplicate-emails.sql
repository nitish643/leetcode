# Write your MySQL query statement below
-- select email from person
-- group by email having count(email)>1;
select email AS Email from  Person Group BY email HAVING COUNT(email)>1;