-- -- # Write your MySQL query statement below

-- -- select p.FirstName, p.LastName, a.City, a.State 
-- -- from person p
-- -- left join address a on p.personId = a.personId








-- select p.FirstName, p.LastName, a.City, a.State 
-- from person p
-- left join address a on p.personId = a.personId 










select p.firstName,p.lastName,a.city,a.state
from Person as p
LEFT JOIN Address as a
ON p.personId = a.personId;













