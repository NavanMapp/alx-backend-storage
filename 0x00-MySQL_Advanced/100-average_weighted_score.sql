-- Create a stored procedure to compute and store the average weighted score for a student
--
CREATE PROCEDURE ComputeAverageWeightedScoreForUser
(
    @user_id INT
)
AS
BEGIN
    DECLARE @average_weighted_score FLOAT;

    SELECT @average_weighted_score = COALESCE(AVG(score * weight), 0)
    FROM corrections
    INNER JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = @user_id;

    UPDATE users SET average_score = @average_weighted_score
    WHERE id = @user_id;

    RETURN;
END;
