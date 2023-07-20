-- Lists all cities contained in the database hbtn_0d_usa.
-- Records are sorted in order of ascending cities.id.
SELECT cty.`id`, cty.`name`, ste.`name`
  FROM `cities` AS cty
       INNER JOIN `states` AS ste
       ON cty.`state_id` = ste.`id`
 ORDER BY cty.`id`;
