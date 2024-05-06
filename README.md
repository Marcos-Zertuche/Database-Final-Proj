# Database-Final-Proj

## Description
This project aims to implement a database solution, using mySQL as the backend, to store and evaluate university degree programs.

## Database Schema
![Database Schema](./DB-Final-Project-Schema.png)

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

### Data Entry
The following section will teach you the order in which you are allowed to add entries to the database. Certain entities are dependent on the existence of other entities, such as Section and Course, so those other entities have to be created first. Feel free to open MySQL Command Line Client to verify that the various information have been correctly entered and stored into the database.

#### Add a Level:
- For a Degree to exist, you must first define a Level (BA, BS, MS, Ph.D., Cert, etc.):

![Screenshot 2024-05-05 at 6 48 36 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/fcf19dca-8a35-4162-a0bb-387e89e9abe9)

#### Add a Degree:
- Now that a Level exists, you can define a Degree with that Level:

![Screenshot 2024-05-05 at 6 52 03 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/4ccbc63a-dc8c-4cd8-8aef-77bc5fd24c2f)

#### Add an Instructor:
- Before you can start creating Courses, you must first define some Instructors to teach those Courses:

![Screenshot 2024-05-05 at 6 56 59 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/53d63028-1794-4f32-a931-4125be66b050)

#### Add a Course:
- Let's assign that Instructor you just created to a new Course:
    - Fill out the necessary Course details (ensure the Degree Name and Level matches an existing Degree and Level) and note whether the Course is a Core Course or not. 
    - A Course requires a Section to exist so when you create a new Course, you must also create a new Section for it (ensure the Instructor ID matches an existing Instructor ID).

![Screenshot 2024-05-05 at 7 05 05 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/adf3c50f-8f4a-4ec2-bf08-0ca7d43942c7)

#### Add a Section:
- A Course may have more than one Section, so let's add another Section to the Course we just created:

![Screenshot 2024-05-05 at 7 14 23 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/ccd27899-3480-4fa1-a01b-a61b46b1351b)

#### Add a Learning Objective:
- To evaluate a Degree program, we must define Learning Objectives that their Courses will be evaluated on:

![Screenshot 2024-05-05 at 7 21 03 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/fb0f46d7-7979-4a35-a0b8-4c5efe3ab27e)

#### Add an Evaluation:
- With all the necessary components for an Evaluation created, let's now submit an Evaluation. First, enter the Degree Name, Degree Level, Semester, Year, and Instructor ID for the Course under evaluation:

![Screenshot 2024-05-05 at 7 26 44 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/c282d525-2c1e-4555-83b7-d2ae53a5570a)

- Next, select the Section for which this Evaluation is associated with. We will choose '**Section 001**' for this example run:

![Screenshot 2024-05-05 at 7 30 20 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/70e34121-7f21-410b-b84c-f178d633352d)

- Then, choose the Learning Objective that this Evaluation is assesing (we have only created one Learning Objective thus far):

![Screenshot 2024-05-05 at 11 07 36 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/d75a90fd-7fd7-41c8-b841-bf7d4b2eca17)

- Lastly, enter the grade distribution among the students for that specific Section. Note that entries can be left blank for now and updated later by going through this same process and entering the exact same information:

![Screenshot 2024-05-05 at 7 35 45 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/37be0562-a138-472e-a14a-f04d551b8959)

#### Associate an Existing Learning Objective to a Course:
- A Course may want to associate an existing Learning Objective with it. To show this, let's first create another Course:

![Screenshot 2024-05-05 at 7 49 35 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/811407d2-1b0d-48d6-8228-2c2a3c1abae3)

- Now we can associate our existing Learning Objective '**Querying**' to this new Course:

![Screenshot 2024-05-05 at 7 51 56 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/403d45a5-40bb-4391-b11a-de593a54b75d)

#### Assign Existing Course to a Degree:
- A Course may be part of the curriculum of multiple Degrees. We can establish these associations by entering the Course ID (department code + course number) and the Degree Name and Level. First, let's create a new Degree:

![Screenshot 2024-05-05 at 7 58 06 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/91a35a22-5cc2-4a80-93a1-12b5c47cf383)

- Associate our '**CS5330**' Course with this new Degree:

![Screenshot 2024-05-05 at 8 26 32 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/3d6ad30d-9947-4c32-8f65-8c52173cb4d5)

### Query
We have gone over all the functionalities of the Data-Entry portion. Now let's explore how we can retrieve all the information we have stored.

#### List Courses Given Degree:
- Provide Degree Name and Level to retrieve all Courses associated with the Degree, as well as whether the Course is a Core Course or not:

![Screenshot 2024-05-05 at 10 13 40 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/65ccc5b6-5eda-4cda-8475-a85e66a3786f)

![Screenshot 2024-05-05 at 10 13 24 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/a8f114ab-4b60-412f-8137-8033c409809f)

#### List Sections Given Degree:
- Provide Degree Name, Level, and a time range to retrieve all Sections offered in chronological order:

![Screenshot 2024-05-05 at 10 15 42 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/0ee68d1f-3425-4bca-a84b-e8518b5d253a)

![Screenshot 2024-05-05 at 10 15 49 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/0e9ab0fa-adbc-405e-b9c1-3d61b2f1295a)

#### List Learning Objectives Given Degree:
- Provide Degree Name and Level to retrieve all Learning Objectives associated with the Degree:

![Screenshot 2024-05-05 at 10 17 29 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/f13c0ea6-b470-4b61-8e3f-d051be6e93a2)

![Screenshot 2024-05-05 at 10 17 36 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/f4d32827-9e12-468d-a092-cf16c6ce21e0)

#### List Courses Per Objective Given Degree:
- Provide Degree Name and Level to retrive all Learning Objectives and for each Objective, list the Courses associated with it (can toggle which Objective's Courses to be shown):

![Screenshot 2024-05-05 at 10 19 47 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/193d21c6-45e8-404e-9754-76a603468ccf)

![Screenshot 2024-05-05 at 10 19 57 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/3be147be-7e27-4ea8-ab40-289c0b1ac1f3)

#### List Sections Given Course:
- Provide Course ID (department code + course number) and time range to retrieve all Sections under the Course:

![Screenshot 2024-05-05 at 10 22 35 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/f2f4f30d-5323-4e58-b4c2-7b49ef9fd9c7)

![Screenshot 2024-05-05 at 10 21 46 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/bb778cac-14dd-4e2a-a542-4223539994fa)

#### List Sections Given Instructor:
- Provide Instructor ID and time range to retrieve all Sections that he/she has taught:

![Screenshot 2024-05-05 at 10 24 15 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/f9cd4967-3898-4544-922c-d8df1a53b871)

![Screenshot 2024-05-05 at 10 24 25 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/5038aede-6373-4215-bb02-177bb16fdba4)

#### List Sections Given Semester/Percentage:
- Provide semester, year, and a percentage value to retrieve all Sections where the number of students that did not get the ‘**F**’ grade reached that percentage. In '**Section 001**' of Course '**CS5330**', **28** out of the **30** students did not get the '**F**' grade (~**93.33%**). Let's choose a value above and below this percentage to see how this query will return.

- Choosing a percentage value of '**95**':

![Screenshot 2024-05-05 at 10 28 48 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/9c51bc11-ed8f-46f3-a71a-99a12c5fc0cc)

![Screenshot 2024-05-05 at 10 28 54 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/b26d0a0c-4154-418b-8611-c77977c02940)

- Choosing a percentage value of '**90**':

![Screenshot 2024-05-05 at 10 29 46 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/9334889a-6a66-417e-9ca5-9dd29c55aaae)

![Screenshot 2024-05-05 at 10 29 55 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/82041c3a-9a3d-4c52-8ca2-6775e1b1bb4f)

#### List Sections & Evaluation Status Given Semester:
- Provide semester and year to retrieve all Sections and for each section, state whether the Evaluation objectives have been entered, partially entered, or not entered at all (in regards to A, B, C, F and not the optional Improvement paragraph).

![Screenshot 2024-05-05 at 10 33 27 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/4f952308-1b40-488f-9650-7190b6642228)

![Screenshot 2024-05-05 at 10 33 39 PM](https://github.com/Marcos-Zertuche/Database-Final-Proj/assets/108942845/b5934133-56f4-4d1c-9160-fa170991b7cc)

## That is all! :D
