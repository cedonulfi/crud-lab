# Node.js CRUD Example

This repository contains a simple CRUD (Create, Read, Update, Delete) application built using Node.js, Express, and MySQL. This project demonstrates basic operations to interact with a MySQL database via RESTful APIs.

## Features

- **Create**: Add a new user to the database.
- **Read**: Retrieve a list of users.
- **Update**: Modify user information based on the user ID.
- **Delete**: Remove a user from the database based on the user ID.

## Prerequisites

- [Node.js](https://nodejs.org/) (v14 or newer recommended)
- [MySQL](https://www.mysql.com/)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/cedonulfi/crud-lab.git
   cd crud-lab/nodejs-crud
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure the database:
   - Create a MySQL database named `crud_db`.
   - Create a table `users` with the following schema:
     ```sql
     CREATE TABLE users (
         id INT AUTO_INCREMENT PRIMARY KEY,
         name VARCHAR(255) NOT NULL,
         email VARCHAR(255) NOT NULL
     );
     ```
   - Update the database credentials in `index.js` if needed:
     ```javascript
     const db = mysql.createConnection({
         host: 'localhost',
         user: 'root',
         password: 'password',
         database: 'crud_db'
     });
     ```

## Usage

1. Start the server:
   ```bash
   node index.js
   ```

2. The server will run on `http://localhost:3000`.

3. Use the following endpoints to perform CRUD operations:

   - **Create**: Add a new user
     ```
     POST /users
     Body: {
         "name": "User Name",
         "email": "user@example.com"
     }
     ```

   - **Read**: Retrieve all users
     ```
     GET /users
     ```

   - **Update**: Update a user by ID
     ```
     PUT /users/:id
     Body: {
         "name": "Updated Name",
         "email": "updated@example.com"
     }
     ```

   - **Delete**: Delete a user by ID
     ```
     DELETE /users/:id
     ```

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.
