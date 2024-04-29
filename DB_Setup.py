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
    cursor.execute("DROP TABLE IF EXISTS Level, Degree, Course, Degree_Course, Instructor, LearningObjective, LearningObjective_Course, Section, Evaluation")

    
    # Creating Level table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Level (
            DegreeLevel VARCHAR(5),
            PRIMARY KEY (DegreeLevel)
        );
    """)

    # Creating Degree table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Degree (
            DegreeName VARCHAR(50),
            DegreeLevel VARCHAR(5),
            PRIMARY KEY (DegreeName, DegreeLevel),
            FOREIGN KEY (DegreeLevel) REFERENCES Level(DegreeLevel)
        );
    """)

    # Creating Course table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Course (
            CourseID VARCHAR(8),
            CourseName VARCHAR(50),
            PRIMARY KEY (CourseID)
        );
    """)

    # Creating Degree_Course table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Degree_Course (
            DegreeName VARCHAR(50),
            DegreeLevel VARCHAR(5),
            CourseID VARCHAR(8),
            IsCore BOOLEAN,
            PRIMARY KEY (DegreeName, DegreeLevel, CourseID, IsCore),
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
            FOREIGN KEY (DegreeName, DegreeLevel) REFERENCES Degree(DegreeName, DegreeLevel)
        );
    """)

    # Creating Instructor table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Instructor (
            InstructorID VARCHAR(8),
            InstructorName VARCHAR(50),
            PRIMARY KEY (InstructorID)
        );
    """)

    # Creating LearningObjective table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS LearningObjective (
            ObjectiveCode INT AUTO_INCREMENT PRIMARY KEY,
            ObjectiveTitle VARCHAR(120) UNIQUE,
            Description VARCHAR(500)
        );
    """)

    # Creating LearningObjective_Course table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS LearningObjective_Course (
            LearningObjectiveTitle VARCHAR(120),
            CourseID VARCHAR(8),
            PRIMARY KEY (LearningObjectiveTitle, CourseID),
            FOREIGN KEY (LearningObjectiveTitle) REFERENCES LearningObjective(ObjectiveTitle),
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID)
        );
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
            INDEX section_index (SectionID, Semester, Year),
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
            FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
        );
    """)

    # Creating Evaluation table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Evaluation (
            EvalObjective VARCHAR(50),
            DegreeName VARCHAR(50),
            DegreeLevel VARCHAR(5),
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
            FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
            FOREIGN KEY (SectionID, Semester, Year) REFERENCES Section(SectionID, Semester, Year), 
            FOREIGN KEY (DegreeName, DegreeLevel) REFERENCES Degree(DegreeName, DegreeLevel),
            FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
        );
    """)

    conn.commit()
    conn.close()



# Call the function to create tables when the script is executed
create_tables()


def Insert_Instructor(dict_info):

    conn = connect_db()
    cursor = conn.cursor() 

    Instructor_ID  = dict_info["instructorID"]
    Instructor_Name  = dict_info["instructorName"]
    query = """INSERT INTO Instructor(InstructorID, InstructorName) VALUES (%s, %s)"""
    cursor.execute(query, (Instructor_ID, Instructor_Name))

    conn.commit()
    conn.close
    return

# def Insert_Degree(dict_info):

#     conn = connect_db()
#     cursor = conn.cursor() 

#     Degree_Name  = dict_info["name"]
#     DegreeLevel  = dict_info["level"]
#     cursor.execute("""INSERT INTO Degree(DegreeName, DegreeLevel)
#                    ,"""(Degree_Name, DegreeLevel))

#     conn.commit()
#     conn.close
#     return
    

# def Insert_Course(dict_info):


# def Insert_Section(dict_info):


# def Insert_Learning_Objective(dict_info):



# def Insert_Level(dict_info):