USE django_db;
-- automatically create a new user-client entity in the table while being ACID compliant
DROP PROCEDURE IF EXISTS new_client;
DELIMITER //
CREATE PROCEDURE new_client(l_name VARCHAR(255), f_name VARCHAR(255), email VARCHAR(255), address_id INT, phone_num INT, role_id INT, pw VARCHAR(255))
	DETERMINISTIC
    BEGIN
		DECLARE id INT;
        DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
			-- returns the mysql error if the function exits with an exception
			GET CURRENT DIAGNOSTICS CONDITION 1 error_no = MYSQL_ERRNO;
			SELECT error_no AS mysql_error;
			ROLLBACK;
		END;
		START TRANSACTION;
			INSERT INTO users VALUES();
			SET id = LAST_INSERT_ID();
			INSERT INTO auth  VALUES (id, pw);
			INSERT INTO clients VALUES(id, f_name, l_name, email, address_id, phone-num, 0);
			INSERT INTO has_role VALUES(id, 2);
        COMMIT;
    END\\
DELIMITER ;
  