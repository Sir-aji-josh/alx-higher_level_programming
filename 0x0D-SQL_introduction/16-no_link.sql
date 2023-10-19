-- List all records of 'second_table' of db 'hbtn_0c_0'
-- Records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
