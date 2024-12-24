# Load the mysql2 gem for interacting with the MySQL database
require 'mysql2'

# Establish connection to the database
client = Mysql2::Client.new(
  host: 'localhost',
  username: 'root',
  password: 'password',
  database: 'crud_db'
)

# Menu-driven CRUD operations
def menu
  puts "\n=== Ruby MySQL CRUD ==="
  puts "1. Create User"
  puts "2. Read Users"
  puts "3. Update User"
  puts "4. Delete User"
  puts "5. Exit"
  print "Choose an option: "
end

loop do
  menu
  option = gets.chomp.to_i

  case option
  when 1
    # Create User
    print "Enter name: "
    name = gets.chomp
    print "Enter email: "
    email = gets.chomp
    client.query("INSERT INTO users (name, email) VALUES ('#{name}', '#{email}')")
    puts "User added successfully!"
  when 2
    # Read Users
    results = client.query("SELECT * FROM users")
    puts "\n--- Users List ---"
    results.each do |row|
      puts "ID: #{row['id']}, Name: #{row['name']}, Email: #{row['email']}"
    end
  when 3
    # Update User
    print "Enter user ID to update: "
    id = gets.chomp
    print "Enter new name: "
    name = gets.chomp
    print "Enter new email: "
    email = gets.chomp
    client.query("UPDATE users SET name='#{name}', email='#{email}' WHERE id=#{id}")
    puts "User updated successfully!"
  when 4
    # Delete User
    print "Enter user ID to delete: "
    id = gets.chomp
    client.query("DELETE FROM users WHERE id=#{id}")
    puts "User deleted successfully!"
  when 5
    # Exit
    puts "Exiting... Goodbye!"
    break
  else
    puts "Invalid option! Please choose again."
  end
end

# Close the database connection
client.close
