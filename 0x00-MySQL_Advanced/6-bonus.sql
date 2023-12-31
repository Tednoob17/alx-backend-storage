-- Creates a stored procedure AddBonus that adds a new correction
DELIMITER $$;
CREATE PROCEDURE AddBonus(
	IN user_id INTEGER,
	IN project_name VARCHAR(255),
	IN score INTEGER
)
END;$$
DELIMITER;
