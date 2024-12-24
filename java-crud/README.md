# Java CRUD with MySQL

This project demonstrates a basic implementation of CRUD (Create, Read, Update, Delete) operations in Java using a MySQL database. The application connects to the database, allowing users to manage a `users` table with functionality to add, view, update, and delete records.

## Features
- **Create**: Add a new user with `name` and `email`.
- **Read**: Retrieve and display all users from the database.
- **Update**: Modify the `name` and `email` of an existing user by ID.
- **Delete**: Remove a user from the database by ID.

## Prerequisites
1. **Java Development Kit (JDK)**: Ensure you have JDK 8 or later installed.
2. **MySQL Server**: Install and configure MySQL.
3. **JDBC Driver**: The MySQL Connector/J library must be added to your project.
   - You can download it from [MySQL Connector/J](https://dev.mysql.com/downloads/connector/j/).

## Setup
### Database Setup
1. Create the database and table using the provided `db.sql` file:
   ```sql
   CREATE DATABASE crud_db;
   USE crud_db;
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100),
       email VARCHAR(100)
   );
   ```

### Project Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/cedonulfi/crud-lab.git
   cd crud-lab/java-crud
   ```
2. Add the MySQL Connector/J JAR file to your classpath.
   
3. Update the database credentials in `JavaMySQLCRUD.java`:
   ```java
   private static final String URL = "jdbc:mysql://localhost:3306/crud_db";
   private static final String USER = "root";
   private static final String PASSWORD = "password";
   ```

4. Compile and run the program:
   ```bash
   javac JavaMySQLCRUD.java
   java JavaMySQLCRUD
   ```

## Usage
Follow the on-screen menu to perform CRUD operations:
- **Create User**: Add a new user to the database.
- **Read Users**: View all existing users.
- **Update User**: Edit the `name` and `email` of a user by specifying their ID.
- **Delete User**: Remove a user by specifying their ID.

## License
This project is licensed under the [MIT License](LICENSE).

## Contribution
Feel free to fork the repository and submit pull requests for any enhancements or bug fixes.

---

### Author
Created by [cedonulfi](https://github.com/cedonulfi).
