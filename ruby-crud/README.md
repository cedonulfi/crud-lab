# Ruby CRUD with MySQL

This project demonstrates a simple implementation of CRUD (Create, Read, Update, Delete) operations using Ruby and a MySQL database. The script interacts with the `users` table in a `crud_db` database.

## Features
- **Create**: Add a new user with `name` and `email`.
- **Read**: View all users in the database.
- **Update**: Edit the `name` and `email` of an existing user by specifying their ID.
- **Delete**: Remove a user from the database by specifying their ID.

## Prerequisites
1. **Ruby**: Ensure Ruby is installed on your system (version 2.5 or later recommended).
2. **MySQL Server**: Install and configure MySQL.
3. **MySQL2 Gem**: The Ruby `mysql2` gem must be installed.

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
   cd crud-lab/ruby-crud
   ```
2. Install the `mysql2` gem:
   ```bash
   gem install mysql2
   ```
3. Update the database credentials in `ruby_mysql_crud.rb`:
   ```ruby
   client = Mysql2::Client.new(
     host: 'localhost',
     username: 'root',
     password: 'password',
     database: 'crud_db'
   )
   ```

4. Run the script:
   ```bash
   ruby ruby_mysql_crud.rb
   ```

## Usage
Follow the menu displayed in the terminal to perform CRUD operations:
- **1. Create User**: Add a new user to the database.
- **2. Read Users**: Display all existing users.
- **3. Update User**: Modify a user's `name` and `email` by specifying their ID.
- **4. Delete User**: Remove a user by specifying their ID.
- **5. Exit**: Exit the program.

## License
This project is licensed under the [MIT License](LICENSE).

## Contribution
Contributions are welcome! Fork the repository and submit a pull request for any enhancements or bug fixes.

---

### Author
Created by [cedonulfi](https://github.com/cedonulfi).
