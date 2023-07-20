-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title, tv_show_genres.genre_id.
SELECT ste.`title`, g.`genre_id`
  FROM `tv_shows` AS ste
        INNER JOIN `tv_show_genres` AS g
	ON ste.`id` = g.`show_id`
 ORDER BY ste.`title`, g.`genre_id`;
