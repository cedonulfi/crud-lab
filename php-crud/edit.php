<?php
include 'connection.php';

$id = $_GET['id'];
$query = "SELECT * FROM users WHERE id = $id";
$result = $conn->query($query);
$user = $result->fetch_assoc();

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $name = $_POST['name'];
    $address = $_POST['address'];
    $email = $_POST['email'];

    $query = "UPDATE users SET name = '$name', address = '$address', email = '$email' WHERE id = $id";
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
    <title>Edit User</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Edit User</h1>
        <form action="" method="POST">
            <label>Name:</label>
            <input type="text" name="name" value="<?php echo $user['name']; ?>" required>
            <label>Address:</label>
            <input type="text" name="address" value="<?php echo $user['address']; ?>" required>
            <label>Email:</label>
            <input type="email" name="email" value="<?php echo $user['email']; ?>" required>
            <button type="submit" class="btn">Save Changes</button>
        </form>
    </div>
</body>
</html>