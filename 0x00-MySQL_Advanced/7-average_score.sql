-- A STORED PROCEDURE THAT COMPUTES AND STORE THE AVERAGE SCORE FOR A STUDENT
DELIMITER $$
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser $$
CREATE
	DEFINER = CURRENT_USER()
	PROCEDURE ComputeAverageScoreForUser(IN user_id INT, OUT average FLOAT)
	BEGIN
		DECLARE total_score, project_count INT DEFAULT 0;
		SELECT COUNT(project_id) INTO project_count
			FROM corrections
			WHERE corrections.user_id = user_id;
		SELECT corrections
			SET total_score = total_score + score
			WHERE corrections.user_id = user_id;	
		SET average = total_score / project_count;
		UPDATE users
			SET average_score = average
			WHERE id = user_id;
	END;
$$
DELIMITER ;
