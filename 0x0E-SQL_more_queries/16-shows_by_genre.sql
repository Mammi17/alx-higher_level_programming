-- Lists all shows and genres linked to the show from the database
--hbtn_0d_tvshows. Records are ordered ascending show title and genre name
SELECT tle.`title`, g.`name`
  FROM `tv_shows` AS tle
         LEFT JOIN `tv_show_genres` AS sh
	        ON tle.`id` = sh.`show_id`

       LEFT JOIN `tv_genres` AS g
              ON sh.`genre_id` = g.`id`
	       ORDER BY tle.`title`, g.`name`;
