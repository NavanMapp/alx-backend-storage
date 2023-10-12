CREATE PROCEDURE AddBonus
(
    @user_id INT,
    @project_name VARCHAR(255),
    @score INT
)
AS
BEGIN
    DECLARE @project_id INT;

    -- Check if the project already exists
    SELECT @project_id = id FROM projects WHERE name = @project_name;

    -- If the project does not exist, create it
    IF @project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (@project_name);
        SET @project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the new correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (@user_id, @project_id, @score);

    RETURN;
END;
