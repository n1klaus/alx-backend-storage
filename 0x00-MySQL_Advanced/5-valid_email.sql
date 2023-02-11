-- TRIGGER TO RESET THE ATTRIBUTE 'valid_email' ONLY WHEN EMAIL HAS CHANGED
DELIMITER $$
DROP TRIGGER IF EXISTS users.reset_validation $$
CREATE TRIGGER reset_validation
	AFTER UPDATE ON users.email
	FOR EACH ROW
	SET valid_email = 0;
$$
DELIMITER ;