-- Script that creates a trigger that resets the attribute
-- valid_email only when the email has been changed.
DELIMITER $$;
CREATE TRIGGER validate BEFORE UPDATE ON users
FOR EACH ROW

END;$$
DELIMITER;
