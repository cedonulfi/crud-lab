package main

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

// Struct to represent a user
// Adjust this based on your table structure
type User struct {
	ID    int
	Name  string
	Email string
}

func main() {
	// Set up the database connection (update credentials as needed)
	dsn := "username:password@tcp(localhost:3306)/your_database"
	db, err := sql.Open("mysql", dsn)
	if err != nil {
		log.Fatal("Error connecting to the database:", err)
	}
	defer db.Close()

	// Test the database connection
	if err := db.Ping(); err != nil {
		log.Fatal("Error pinging the database:", err)
	}
	fmt.Println("Database connection established.")

	// Uncomment the function calls below to test CRUD operations

	// Create a new user
	// createUser(db, "John Doe", "john.doe@example.com")

	// Read users from the database
	// users := readUsers(db)
	// fmt.Println(users)

	// Update a user's information
	// updateUser(db, 1, "Jane Doe", "jane.doe@example.com")

	// Delete a user
	// deleteUser(db, 1)
}

// Create a new user in the database
func createUser(db *sql.DB, name string, email string) {
	query := "INSERT INTO users (name, email) VALUES (?, ?)"
	_, err := db.Exec(query, name, email)
	if err != nil {
		log.Fatal("Error inserting user:", err)
	}
	fmt.Println("User added successfully.")
}

// Read users from the database
func readUsers(db *sql.DB) []User {
	query := "SELECT id, name, email FROM users"
	rows, err := db.Query(query)
	if err != nil {
		log.Fatal("Error reading users:", err)
	}
	defer rows.Close()

	var users []User
	for rows.Next() {
		var user User
		if err := rows.Scan(&user.ID, &user.Name, &user.Email); err != nil {
			log.Fatal("Error scanning row:", err)
		}
		users = append(users, user)
	}
	return users
}

// Update a user's information in the database
func updateUser(db *sql.DB, id int, name string, email string) {
	query := "UPDATE users SET name = ?, email = ? WHERE id = ?"
	_, err := db.Exec(query, name, email, id)
	if err != nil {
		log.Fatal("Error updating user:", err)
	}
	fmt.Println("User updated successfully.")
}

// Delete a user from the database
func deleteUser(db *sql.DB, id int) {
	query := "DELETE FROM users WHERE id = ?"
	_, err := db.Exec(query, id)
	if err != nil {
		log.Fatal("Error deleting user:", err)
	}
	fmt.Println("User deleted successfully.")
}
