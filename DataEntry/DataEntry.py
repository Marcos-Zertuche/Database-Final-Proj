from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


# Function to connect to MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Impulsive1@",
        database="db_final_project"
    )


# Function to create tables in the database
def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Creating Evaluation table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Evaluation (
            EvaluationID VARCHAR(6) PRIMARY KEY,
            EvalMethod VARCHAR(50),
            ObjectiveCode VARCHAR(6),
            DegreeName VARCHAR(50),
            DegreeLevel VARCHAR(10),
            A INT,
            B INT,
            C INT,
            D INT,
            Description VARCHAR(500),
            InstructorID VARCHAR(8),
            SectionID VARCHAR(3),
            SemesterID VARCHAR(6),
            CourseID VARCHAR(8)
        )
    """)

    # Creating Degree table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Degree (
            DegreeName VARCHAR(50),
            DegreeLevel VARCHAR(5),
            PRIMARY KEY (DegreeName, DegreeLevel)
        )
    """)
    # Creating Course table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Course (
            CourseID VARCHAR(8),
            CourseName VARCHAR(50),
            CoreClass BOOLEAN,
            DegreeName VARCHAR(50),
            DegreeLevel VARCHAR(5),
            PRIMARY KEY (CourseID),
            FOREIGN KEY (DegreeName, DegreeLevel) REFERENCES Degree(DegreeName, DegreeLevel)
        )
    """)


    # Creating LearningObjective table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS LearningObjective (
            CourseID VARCHAR(8),
            ObjectiveCode VARCHAR(6),
            ObjectiveTitle VARCHAR(120),
            Description VARCHAR(500),
            PRIMARY KEY (CourseID, ObjectiveCode),
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
        )
    """)

    # Creating Level table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Level (
            LevelName VARCHAR(5),
            PRIMARY KEY (LevelName)
        )
    """)

    # Creating Section table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Section (
            SectionID VARCHAR(3),
            SemesterID VARCHAR(6),
            CourseID VARCHAR(8),
            NumStudents INT,
            InstructorID VARCHAR(8),
            PRIMARY KEY (SectionID, SemesterID, CourseID),
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
        )
    """)

    
    # Creating Instructor table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Instructor (
            InstructorID VARCHAR(8),
            InstructorName VARCHAR(50),
            PRIMARY KEY (InstructorID)
        )
    """)

    conn.commit()
    conn.close()


# Call the function to create tables when the script is executed
create_tables()


@app.route('/data-entry')
def home():
    return render_template('data-entry.html')


@app.route('/add-degree', methods=['GET', 'POST'])
def add_degree():
    if request.method == 'POST':
        # Connect to the database
        conn = connect_db()
        cursor = conn.cursor()

        # Process the submitted form data
        degree_name = request.form['degree_name']
        degree_level = request.form['degree_level']

        # Insert data into Degree table
        cursor.execute("INSERT INTO Degree (DegreeName, DegreeLevel) VALUES (%s, %s)", (degree_name, degree_level))
        conn.commit()
        conn.close()

        return "Degree information submitted successfully!"
    else:
        return render_template('./Degree/add-degree-form.html')


@app.route('/add-course', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        # Connect to the database
        conn = connect_db()
        cursor = conn.cursor()

        # Process the submitted form data
        course_id = request.form['course_id']
        course_name = request.form['course_name']
        core_class = request.form['core_class']
        degree_name = request.form['degree_name']
        degree_level = request.form['degree_level']

        # Insert data into Course table
        cursor.execute("INSERT INTO Course (CourseID, CourseName, CoreClass, DegreeName, DegreeLevel) VALUES (%s, %s, %s, %s, %s)",
                       (course_id, course_name, core_class, degree_name, degree_level))
        conn.commit()
        conn.close()

        return "Course information submitted successfully!"
    else:
        return render_template('./Course/add-course-form.html')


# Add other routes and functions as needed

if __name__ == '__main__':
    app.run(debug=True)
