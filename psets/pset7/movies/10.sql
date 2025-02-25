SELECT name FROM people
JOIN directors ON people.id = directors.person_id
JOIN movies ON ratings.movie_id = movies.id
Join ratings ON directors.movie_id = ratings.movie_id
WHERE ratings.rating >= 9.0;