import mysql.connector
import json

# Connect to the database
def connect_db():
    with open('./config.json', 'r') as f:
        config = json.load(f)
    f.close()
    
    return mysql.connector.connect(
        host=config['host'],
        user=config['user'],
        password=config['password'],
        database=config['database']
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
            EvalObjective VARCHAR(50),
            DegreeName VARCHAR(50),
            DegreeLevel VARCHAR(10),
            A INT,
            B INT,
            C INT,
            F INT,
            EvaluationDescription VARCHAR(500),
            InstructorID VARCHAR(8),
            SectionID VARCHAR(3),
            Semester VARCHAR(6),
            Year INT,
            CourseID VARCHAR(8),
            PRIMARY KEY (SectionID, CourseID, EvalObjective), 
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
            FOREIGN KEY (SectionID, Semester, Year) REFERENCES Section(SectionID, Semester, Year) 
            FOREIGN KEY (DegreeName, DegreeLevel) REFERENCES Degree(DegreeName, DegreeLevel)
            FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
            
        )
    """)

    # Creating Degree table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Degree (
            DegreeName VARCHAR(50),
            DegreeLevel VARCHAR(5),
            PRIMARY KEY (DegreeName, DegreeLevel)
            FOREIGN KEY (DegreeLevel) REFERENCES Level(DegreeLevel)
        )
    """)

    # Creating LearningObjective table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS LearningObjective (
            ObjectiveCode VARCHAR(6) AUTO_INCREMENT,
            ObjectiveTitle VARCHAR(120),
            Description VARCHAR(500),
            PRIMARY KEY (ObjectiveCode),
            UNIQUE (ObjectiveTitle),
            FOREIGN KEY (ObjectiveCode) REFERENCES Course(ObjectiveCode)
        )
    """)

    # LearningObjective - Course
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS LearningObjective (
            ObjectiveCode VARCHAR(6),
            CourseID VARCHAR(8)
        )
    """)

    # Creating Level table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Level (
            DegreeLevel VARCHAR(5),
            PRIMARY KEY (DegreeLevel)
            
        )
    """)

    # Creating Section table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Section (
            SectionID VARCHAR(3),
            Semester VARCHAR(6),
            Year INT,
            CourseID VARCHAR(8),
            NumStudents INT,
            InstructorID VARCHAR(8),
            PRIMARY KEY (SectionID, Semester, CourseID, Year),
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
        )
    """)

    # Creating Course table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Course (
            CourseID VARCHAR(8),
            CourseName VARCHAR(50),
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
            CourseID VARCHAR(10),
            IsCore BOOLEAN,
            DegreeLevel VARCHAR(5),
            PRIMARY KEY (DegreeID, CourseID, IsCore,DegreeLevel),
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
);
    """)

    conn.commit()
    conn.close()



# Call the function to create tables when the script is executed
create_tables()