SELECT title
FROM movies
INNER JOIN stars ON stars.movie_id = movies.id
INNER JOIN people ON stars.person_id = people.id
WHERE name = "Johnny Depp" OR name = "Helena Bonham Carter"
GROUP BY movies.id HAVING COUNT(*) > 1;