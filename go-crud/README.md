# Go CRUD Example

This repository contains a simple CRUD (Create, Read, Update, Delete) example built with Go and MySQL. It demonstrates how to connect to a MySQL database and perform basic operations on a `users` table.

## Features

- **Create**: Add new users to the database.
- **Read**: Retrieve all users from the database.
- **Update**: Modify existing user information.
- **Delete**: Remove a user from the database.

## Prerequisites

1. **Go**: Ensure you have Go installed on your system. You can download it from [golang.org](https://golang.org/dl/).
2. **MySQL**: Install and set up a MySQL server.
3. **Database Setup**: Create a MySQL database and table using the script below:

```sql
CREATE DATABASE your_database;
USE your_database;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/cedonulfi/crud-lab.git
   cd crud-lab/go-crud
   ```

2. Install dependencies:
   ```bash
   go get -u github.com/go-sql-driver/mysql
   ```

3. Update database credentials in `main.go`:
   ```go
   dsn := "username:password@tcp(localhost:3306)/your_database"
   ```

   Replace `username`, `password`, `localhost`, and `your_database` with your MySQL details.

4. Run the application:
   ```bash
   go run main.go
   ```

## Usage

- To test CRUD operations, uncomment the respective function calls in the `main` function of `main.go`.

## Project Structure

```
crud-lab/
├── go-crud/
│   ├── main.go
│   └── README.md
```

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests to improve this project.

## Author

Created by **Cedonulfi**.
