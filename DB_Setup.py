import mysql.connector

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

    # Drop the sample_table if it exists
    cursor.execute("DROP TABLE IF EXISTS sample_table")

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

    # Creating Course table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Course (
            CourseID VARCHAR(8),
            CourseName VARCHAR(50),
            DegreeName VARCHAR(50),
            DegreeLevel VARCHAR(5),
            PRIMARY KEY (CourseID),
            FOREIGN KEY (DegreeName, DegreeLevel) REFERENCES Degree(DegreeName, DegreeLevel)
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

    # Creating Degree_Course table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Degree_Course (
            DegreeID INT AUTO_INCREMENT,
            CourseNum VARCHAR(10),
            IsCore BOOLEAN,
            PRIMARY KEY (DegreeID, CourseNum, IsCore),
            FOREIGN KEY (CourseNum) REFERENCES Course(CourseID)
);
    """)

    conn.commit()
    conn.close()



# Call the function to create tables when the script is executed
create_tables()