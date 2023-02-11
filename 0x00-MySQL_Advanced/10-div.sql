-- FUNCTION THAT DIVIDES AND RETURNS THE FIRST BY THE SECOND NUMBER
-- OR RETURNS 0 IF THE SECOND NUMBER IS EQUAL TO 0
DELIMITER $$
DROP FUNCTION IF EXISTS safeDiv $$
CREATE 
	DEFINER = CURRENT_USER()
	FUNCTION safeDiv(a INT, b INT)
	BEGIN
		IF b = 0 THEN
			RETURN 0;
		ELSE	
			RETURN a * b;
		END IF;
	END;
$$ 
DELIMITER ;