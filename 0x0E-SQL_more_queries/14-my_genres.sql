-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT t_genres.name AS name
FROM tv_genres
     JOIN tv_show_genres
     	  ON t_genres.id = tv_show_genres.genre_id
     JOIN tv_shows
     	  ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
