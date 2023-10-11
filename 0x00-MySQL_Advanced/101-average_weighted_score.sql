DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE user_avg_score FLOAT;

    -- Initialize variables
    SET user_id = 0;
    SET total_weighted_score = 0;
    SET total_weight = 0;

    -- Loop through all users
    users_loop: LOOP
        -- Find the next user
        SELECT id INTO user_id FROM users WHERE id > user_id LIMIT 1;
        IF user_id IS NULL THEN
            LEAVE users_loop;
        END IF;

        -- Calculate the total weighted score for the user
        SET total_weighted_score = 0;
        SET total_weight = 0;

        -- Calculate the total weighted score for the user
        SELECT SUM(c.score * p.weight) INTO total_weighted_score
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Calculate the total weight for the user
        SELECT SUM(p.weight) INTO total_weight
        FROM projects p
        JOIN corrections c ON p.id = c.project_id
        WHERE c.user_id = user_id;

        -- Calculate the average weighted score for the user
        IF total_weight > 0 THEN
            SET user_avg_score = total_weighted_score / total_weight;
        ELSE
            SET user_avg_score = 0;
        END IF;

        -- Update the user's average_score in the users table
        UPDATE users
        SET average_score = user_avg_score
        WHERE id = user_id;
    END LOOP;
END //
DELIMITER ;
