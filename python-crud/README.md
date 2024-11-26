# Python CRUD

This is the Python implementation of a CRUD application included in the [CRUD-Lab](https://github.com/cedonulfi/crud-lab) repository. It uses **Flask** as the web framework and **SQLite** as the database.

## Features

- Perform basic CRUD operations (Create, Read, Update, Delete) on a `user` table.
- Responsive HTML templates for the interface.
- Lightweight and easy to set up.

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.7 or newer
- `pip` package manager

## Installation

1. Clone the repository and navigate to the `python-crud` directory:
   ```bash
   git clone https://github.com/cedonulfi/crud-lab.git
   cd crud-lab/python-crud
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install flask
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and go to http://localhost:5000.



## Project Structure

```bash
python-crud/
├── app.py              # Main application file
├── templates/
│   ├── index.html      # HTML for displaying user data
│   └── update.html     # HTML for updating user data
└── README.md           # This file
```

## How to Use

1. Create a New User: Fill in the form on the homepage and click "Add User".

2. Edit a User: Click "Edit" on the user table, modify the details, and save.

3. Delete a User: Click "Delete" on the user table to remove the user.


## Notes

The database (database.db) will be created automatically when you run the app.

Data is stored locally using SQLite.


## License

This project is part of the CRUD-Lab repository and is distributed under the MIT License. See the LICENSE file for more details.


