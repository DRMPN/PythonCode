SELECT AVG(rating)
FROM ratings
INNER JOIN movies ON movies.id = ratings.movie_id
WHERE year = 2012;