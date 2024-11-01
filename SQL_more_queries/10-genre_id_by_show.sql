-- Selects Title from tv_shows and genre_id from tv_show_genres
-- Then Joins tv_show_genres looking through tv_show_genres with tv_show_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
