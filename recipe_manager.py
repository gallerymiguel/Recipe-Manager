import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into environment

conn = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST'),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    database=os.getenv('MYSQL_DATABASE')
)

cursor = conn.cursor()


# Function: List all recipes
def list_recipes():
    cursor.execute("SELECT id, name, description FROM recipes")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Description: {row[2]}")

# Function: Add a recipe
def add_recipe(name, description):
    cursor.execute("INSERT INTO recipes (name, description) VALUES (%s, %s)", (name, description))
    conn.commit()
    print("Recipe added!")
    
# Function: Update a recipe
def update_recipe(recipe_id, new_name, new_description):
    sql = "UPDATE recipes SET name = %s, description = %s WHERE id = %s"
    cursor.execute(sql, (new_name, new_description, recipe_id))
    conn.commit()
    print("Recipe updated!")
    
# Function: Delete a recipe by ID
def delete_recipe(recipe_id):
    sql = "DELETE FROM recipes WHERE id = %s"
    cursor.execute(sql, (recipe_id,))
    conn.commit()
    print(f"Recipe with ID {recipe_id} deleted!")

# Function: Search recipes by name (case-insensitive)
def search_recipes(search_term):
    sql = "SELECT id, name, description FROM recipes WHERE name LIKE %s"
    # The % in the parameter allows for partial matches before and after the search_term
    wildcard_search = f"%{search_term}%"
    cursor.execute(sql, (wildcard_search,))
    results = cursor.fetchall()
    if results:
        print(f"Recipes matching '{search_term}':")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Description: {row[2]}")
    else:
        print(f"No recipes found matching '{search_term}'.")


# ---------
# Example usage:
list_recipes()
add_recipe("Test Recipe", "This is just a test!")

print("\nAfter adding a recipe:")
list_recipes()

update_recipe(4, "Updated Test Recipe", "Now this description is updated!")  

delete_recipe(4)  

print("\nAfter deleting a recipe:")
list_recipes()

print("\nAfter updating a recipe:")
list_recipes()

print("\nSearch results:")
search_recipes("Test")


#Clean up
cursor.close()
conn.close()

