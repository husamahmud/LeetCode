-- Write your PostgreSQL query statement below
select firstName as "firstName",lastname "lastName",city,state 
from person left join address
on person.personid=address.personid