const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

const db = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'password',
    database: 'crud_db'
});

db.connect(err => {
    if (err) {
        throw err;
    }
    console.log('MySQL Connected...');
});

// Create
app.post('/users', (req, res) => {
    const user = { name: req.body.name, email: req.body.email };
    const sql = 'INSERT INTO users SET ?';
    db.query(sql, user, (err, result) => {
        if (err) throw err;
        res.send('User added...');
    });
});

// Read
app.get('/users', (req, res) => {
    const sql = 'SELECT * FROM users';
    db.query(sql, (err, results) => {
        if (err) throw err;
        res.json(results);
    });
});

// Update
app.put('/users/:id', (req, res) => {
    const { id } = req.params;
    const { name, email } = req.body;
    const sql = `UPDATE users SET name='${name}', email='${email}' WHERE id=${id}`;
    db.query(sql, (err, result) => {
        if (err) throw err;
        res.send('User updated...');
    });
});

// Delete
app.delete('/users/:id', (req, res) => {
    const { id } = req.params;
    const sql = `DELETE FROM users WHERE id=${id}`;
    db.query(sql, (err, result) => {
        if (err) throw err;
        res.send('User deleted...');
    });
});

app.listen(3000, () => {
    console.log('Server started on port 3000');
});