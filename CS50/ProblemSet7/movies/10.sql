SELECT DISTINCT people.name
FROM people
INNER JOIN directors ON people.id = person_id
INNER JOIN ratings ON directors.movie_id = ratings.movie_id
INNER JOIN movies on directors.movie_id = movies.id
WHERE ratings.rating >= 9.0;