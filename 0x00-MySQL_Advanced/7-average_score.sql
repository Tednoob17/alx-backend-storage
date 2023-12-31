-- Creates a stored procedure ComputeAverageScoreForUser that computes the avg score
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$;
CREATE PROCEDURE ComputeAverageScoreForUser(
	IN user_id INT
)
BEGIN
	UPDATE users
   	SET average_score=(SELECT AVG(score) FROM corrections

END;$$
DELIMITER ;
