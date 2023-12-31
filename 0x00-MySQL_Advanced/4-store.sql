-- Creates a trigger that decreases quantity of an item
CREATE TRIGGER decrease_q AFTER INSERT ON orders FOR EACH ROW

