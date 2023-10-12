-- Get the average weighted score for all students
--
UPDATE users SET average_score = COALESCE(AVG(score * weight), 0)
FROM corrections
INNER JOIN projects ON corrections.project_id = projects.id
GROUP BY users.id;
