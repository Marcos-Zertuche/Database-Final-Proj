# Database-Final-Proj

## Description
This project aims to implement a database solution, using mySQL as the backend, to store and evaluate university degree programs.

## Installation

### Python
1. If you haven't already, download and install Python from [Python's official website](https://www.python.org).
2. Make sure to check the box that says "Add Python to PATH" during installation.
3. Verify the installation by opening a command prompt or terminal and typing '**python --version**'. You should see the installed Python version.

### MySQL
1. Download and install MySQL from [MySQL's official website](https://www.mysql.com).
2. During installation, note down the password you set for the root user.
3. After installation, open MySQL Command Line Client and enter the root password when prompted:

#### Windows:
- Click on the Start menu.
- Type "MySQL Command Line Client" and press Enter.
- Enter the root password when prompted.

#### macOS:
- Open Terminal.
- Type the following command and press Enter:
```
mysql -u root -p
```
- You'll be prompted to enter the root password. Type the password and press Enter.

#### Linux:
- Open Terminal.
- Type the following command and press Enter:
```
sudo mysql -u root -p
```
- You'll be prompted to enter the root password. Type the password and press Enter.

4. Execute the following SQL commands to create a database and a user based on the configuration provided in '**config.json**':
```
CREATE DATABASE db_final_project;
CREATE USER 'root'@'localhost' IDENTIFIED BY 'psw';
GRANT ALL PRIVILEGES ON db_final_project.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
```

### MySQL Connector
1. Install MySQL Connector for Python using pip, Python's package manager, by running the following command:
```
pip install mysql-connector-python
```

### Flask
1. Install Flask using pip by running the following command:
```
pip install Flask
```

### Configuration
Before running the application, make sure the '**config.json**' file contains the appropriate database connection details:
```
{
    "host": "localhost",
    "user": "root",
    "password": "psw",
    "database": "db_final_project"
}
```

## Usage
To run the application, navigate to the project directory in the command prompt or terminal and execute the following commands:
```
python DB_Setup.py
python GUI.py
```
This will create the appropriate tables in the '**db_final_project**' database and then start the Flask application. You should be able to access it through a web browser at '**http://127.0.0.1:5000**'.
