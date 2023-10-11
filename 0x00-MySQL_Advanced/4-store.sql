-- Create the trigger to update the quantity in the 'items'
-- table after inserting a new order
DELIMITER $$
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity of the item in 'items' based on the new order
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
$$
DELIMITER ;
