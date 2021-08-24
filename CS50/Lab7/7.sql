SELECT AVG(energy)
FROM songs
INNER JOIN artists ON songs.artist_id = artists.id
WHERE artists.name = "Drake";

/* alternative version
SELECT AVG(energy)
FROM songs
WHERE artist_id = (SELECT id FROM artists WHERE name = "Drake");
*/