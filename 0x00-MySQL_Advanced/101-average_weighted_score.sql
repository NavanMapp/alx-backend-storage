-- Write a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    -- Declare variables for user and project counts
    DECLARE user_count INT;
    DECLARE project_count INT;
    DECLARE user_id INT;
    DECLARE project_id INT;
    DECLARE total_weighted_score FLOAT;
    DECLARE weighted_avg FLOAT;

    -- Get the total number of users and projects
    SELECT COUNT(*) INTO user_count FROM users;
    SELECT COUNT(*) INTO project_count FROM projects;

    -- Initialize the user_id and project_id
    SET user_id = 1;
    SET project_id = 1;

    -- Loop through each user
    WHILE user_id <= user_count DO
        -- Initialize the total weighted score for the user
        SET total_weighted_score = 0;

        -- Loop through each project for the user
        WHILE project_id <= project_count DO
            -- Calculate the weighted score for the current project and user
            SELECT SUM(score * weight) INTO weighted_avg
            FROM corrections
            INNER JOIN projects ON corrections.project_id = projects.id
            WHERE corrections.user_id = user_id AND corrections.project_id = project_id;

            -- Add the weighted score to the total for the user
            SET total_weighted_score = total_weighted_score + IFNULL(weighted_avg, 0);

            SET project_id = project_id + 1;
        END WHILE;

        -- Calculate the average weighted score for the user
        SET weighted_avg = total_weighted_score / project_count;

        -- Update the user's average_score in the users table
        UPDATE users SET average_score = weighted_avg WHERE id = user_id;

        -- Reset project_id and move to the next user
        SET project_id = 1;
        SET user_id = user_id + 1;
    END WHILE;
END