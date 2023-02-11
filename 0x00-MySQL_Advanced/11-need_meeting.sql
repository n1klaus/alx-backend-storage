-- CREATES A VIEW THAT LISTS ALL STUDENTS THAT HAVE A SCORE UNDER 80
-- and no 'last_meeting' or more than 1 month
CREATE
	OR REPLACE
	DEFINER CURRENT_USER()
	VIEW need_meeting
	AS
	SELECT name
		FROM students
		WHERE score < 80
		AND
		last_meeting = NULL OR DATEDIFF(last_meeting, CURDATE()) > 30;
