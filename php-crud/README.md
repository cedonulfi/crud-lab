# PHP CRUD

This is the PHP implementation of a CRUD application included in the [CRUD-Lab](https://github.com/cedonulfi/crud-lab) repository.

## Features

- Basic CRUD operations for `users` table.
- Responsive and simple UI with pure HTML and CSS.

## How to Use

1. Copy all files to your PHP server directory.
2. Create a database named `crud_db` and a table `users`:
   ```sql
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100),
       address TEXT,
       email VARCHAR(100)
   );
   ```
3. Access the application through your browser.