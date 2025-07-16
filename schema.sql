-- Create the database (if it doesn't already exist)
CREATE DATABASE IF NOT EXISTS recipe_db;
USE recipe_db;

-- Create the recipes table
CREATE TABLE IF NOT EXISTS recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

-- Insert some sample data
INSERT INTO recipes (name, description) VALUES
('Spaghetti Bolognese', 'A classic Italian pasta dish with ground beef, tomato sauce, and herbs.'),
('Chicken Stir Fry', 'Chicken cooked quickly with vegetables and soy sauce in a wok.');


# Example usage:
update_recipe(1, "Updated Spaghetti", "This is the updated description for Spaghetti Bolognese.")
