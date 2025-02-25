select AVG(rating)
from ratings as t1
inner join movies as t2
on (t1.movie_id = t2.id) where t2.year = 2012;