-- A STORED PROCEDURE THAT ADDS A NEW CORRECTION FOR A STUDENT
DELIMITER $$
DROP PROCEDURE IF EXISTS AddBonus $$
CREATE
	DEFINER = CURRENT_USER()
	PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
	BEGIN
		DECLARE project_id INT DEFAULT 0;
		SET project_id = (SELECT id from projects WHERE name = project_name);
		IF project_id = 0 THEN
			INSERT INTO projects (name) VALUES (project_name);
			SET project_id = LAST_INSERT_ID()
		END IF;
		UPDATE corrections
			SET corrections.score = score
			WHERE corrections.user_id = user_id
			AND
			corrections.project_id = project_id;
	END;
$$
DELIMITER ;
