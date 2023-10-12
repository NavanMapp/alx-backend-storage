CREATE PROCEDURE ComputeAverageScoreForUser
(
    @user_id INT
)
AS
BEGIN
    DECLARE @average_score DECIMAL(10,2);

    SELECT @average_score = COALESCE(AVG(score), 0)
    FROM corrections
    WHERE user_id = @user_id;

    UPDATE users SET average_score = @average_score
    WHERE id = @user_id;

    RETURN;
END;
