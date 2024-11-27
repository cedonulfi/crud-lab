<?php
include 'connection.php';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $address = $_POST['address'];
    $email = $_POST['email'];

    $query = "INSERT INTO users (name, address, email) VALUES ('$name', '$address', '$email')";
    if ($conn->query($query)) {
        header('Location: index.php');
    } else {
        echo "Error: " . $conn->error;
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add User</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Add User</h1>
        <form action="" method="POST">
            <label>Name:</label>
            <input type="text" name="name" required>
            <label>Address:</label>
            <input type="text" name="address" required>
            <label>Email:</label>
            <input type="email" name="email" required>
            <button type="submit" class="btn">Add</button>
        </form>
    </div>
</body>
</html>