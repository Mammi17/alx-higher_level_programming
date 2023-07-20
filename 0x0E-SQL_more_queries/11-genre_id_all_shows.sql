-- Lists all shows contained in the database hbtn_0d_tvshows.
-- Displays NULL for shows without genres. Records are ordered by ascending
--tv_shows.title and tv_show_genres.genre_id.
SELECT sh.`title`, g.`genre_id`
  FROM `tv_shows` AS sh
       LEFT JOIN `tv_show_genres` AS g
       ON sh.`id` = g.`show_id`
 ORDER BY sh.`title`, g.`genre_id`;
