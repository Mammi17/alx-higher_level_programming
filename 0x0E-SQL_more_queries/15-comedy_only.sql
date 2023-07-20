-- Lists all comedy shows in the database hbtn_0d_tvshows.
-- Records are ordered descending show title.
SELECT t_shows.title AS title
FROM t_shows
     JOIN tv_show_genres
     	  ON tv_show_genres.show_id = t_shows.id
     JOIN tv_genres
     	  ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title;
