# Recipe Manager (Python + MySQL)

A simple command-line app to manage recipes using Python and MySQL.  
This project was built for learning and practicing database CRUD (Create, Read, Update, Delete) operations with MySQL from Python.

## Features

- **List** all recipes
- **Add** a new recipe
- **Update** a recipe
- **Delete** a recipe
- **Search** recipes by name

## How to Run

1. **Clone this repo** and navigate to the folder.
2. **Install dependencies:**
    ```
    pip install mysql-connector-python python-dotenv
    ```
3. **Set up your database:**  
   - Create a MySQL database called `recipe_db`.
   - Run `schema.sql` to create the `recipes` table.

4. **Create a `.env` file** in the project root with:
    ```
    MYSQL_HOST=localhost
    MYSQL_USER=your_mysql_username
    MYSQL_PASSWORD=your_mysql_password
    MYSQL_DATABASE=recipe_db
    ```

5. **Run the app:**
    ```
    python recipe_manager.py
    ```

## Notes

- All credentials are loaded securely from `.env` (never commit this file!)
- This project is for learning purposes and can be extended with more features.

---

Feel free to adjust anything or let me know if you want to add details (like how to use the functions). Want a quick section on how to use each feature?
