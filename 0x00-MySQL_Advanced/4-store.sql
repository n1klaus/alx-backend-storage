-- DECREASE QUANTITY OF AN ITEM AFTER ADDING A NEW ORDER
DELIMITER $$
CREATE TRIGGER update_quantity
	AFTER INSERT ON orders
	FOR EACH ROW
	BEGIN
		UPDATE items
			SET quantity = quantity - NEW.number
			WHERE NEW.item_name = name;
	END;
$$
DELIMITER ;
