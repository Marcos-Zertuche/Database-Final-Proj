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
    # cursor.execute("DROP TABLE IF EXISTS Level, Degree, Course, Degree_Course, Instructor, LearningObjective, LearningObjective_Course, Section, Evaluation")

#        -- FOREIGN KEY (DegreeLevel) REFERENCES Level(DegreeLevel)

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
            FOREIGN KEY (DegreeName) REFERENCES Degree(DegreeName),
            FOREIGN KEY (DegreeLevel) REFERENCES Level(DegreeLevel)
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

def Insert_Degree(dict_info):

    conn = connect_db()
    cursor = conn.cursor() 

    Degree_Name  = dict_info["name"]
    Degree_Level  = dict_info["level"]

    query = """INSERT INTO Degree(DegreeName, DegreeLevel) VALUES (%s, %s)"""
    cursor.execute(query, (Degree_Name, Degree_Level))

    conn.commit()
    conn.close
    return

def Insert_Level(dict_info):
    conn = connect_db() 
    cursor = conn.cursor()
    print(dict_info)
    Degree_Level = dict_info["levelName"]
    query = """INSERT INTO Level(DegreeLevel) VALUES (%s)"""
    cursor.execute(query,(Degree_Level,))
    
    conn.commit()
    conn.close
    return
    

def Insert_Course(dict_info):
    
    conn = connect_db()
    cursor = conn.cursor() 

    Course_ID  = dict_info["courseDeptCode"] + dict_info["courseNum"]
    Course_Name  = dict_info["courseName"]
    cursor.execute("""INSERT INTO Course(CourseID, CourseName) VALUES (%s, %s)""", (Course_ID, Course_Name))    
    conn.commit()

    # Insert into Degree_Course
    Degree_Name = dict_info["degreeName"]
    Degree_Level = dict_info["degreeLevel"]
    Is_Core = dict_info["isCore"]
    if Is_Core == 'yes':
        Is_Core = 1
    else:
        Is_Core = 0
    cursor.execute("""INSERT INTO Degree_Course(DegreeName, DegreeLevel, CourseID, IsCore) VALUES (%s, %s, %s, %s)""", (Degree_Name, Degree_Level, Course_ID, Is_Core))
    conn.commit()

    # Insert into Section
    Section_ID = dict_info["sectionID"]
    Semester = dict_info["semester"]
    Year = dict_info["year"]
    Num_Students = dict_info["numStudents"]
    Instructor_ID = dict_info["instructorID"]
    cursor.execute("""INSERT INTO Section(SectionID, Semester, Year, CourseID, NumStudents, InstructorID) VALUES (%s, %s, %s, %s, %s, %s)""", (Section_ID, Semester, Year, Course_ID, Num_Students, Instructor_ID))
    conn.commit()

    conn.close
    return


def Insert_Section(dict_info):
    # [('sectionID', '333'), ('courseDeptCode', 'CS'), ('courseNum', '4444'), ('semester', 'Spring'), ('year', '2020'), ('instructorID', '488'), ('numStudents', '3')])
    # Insert into Section
    conn = connect_db()
    cursor = conn.cursor() 
    
    Section_ID = dict_info["sectionID"]
    Semester = dict_info["semester"]
    Year = dict_info["year"]
    Course_ID  = dict_info["courseDeptCode"] + dict_info["courseNum"]
    Num_Students = dict_info["numStudents"]
    Instructor_ID = dict_info["instructorID"]
    
    cursor.execute("""INSERT INTO Section(SectionID, Semester, Year, CourseID, NumStudents, InstructorID) VALUES (%s, %s, %s, %s, %s, %s)""", (Section_ID, Semester, Year, Course_ID, Num_Students, Instructor_ID))
    conn.commit()
    
    conn.close

    return


def Insert_Learning_Objective(dict_info):
    conn = connect_db()
    cursor = conn.cursor() 

    Objective_Title =  dict_info["objectiveTitle"]
    Description = dict_info["objectiveDescription"]
    Course_ID = dict_info["courseID"]
    
    
   # Insert into LearningObjective table
    query = """INSERT INTO LearningObjective(ObjectiveTitle, Description) VALUES (%s, %s)"""
    cursor.execute(query, (Objective_Title, Description))
    conn.commit()
    
    # Insert into LearningObjective_Course table
    query = """INSERT INTO LearningObjective_Course(LearningObjectiveTitle, CourseID) VALUES (%s, %s)"""
    cursor.execute(query, (Objective_Title, Course_ID))
    conn.commit()
    
 
    conn.close
    return

def Get_Courses(dict_info):
     
    conn = connect_db()
    cursor = conn.cursor() 

    print(dict_info)

    Degree_Name =  dict_info["name"]
    Degree_Level = dict_info["level"]
    print(Degree_Name)
    
    query = """
    SELECT c.CourseID, c.CourseName, 
    CASE WHEN dc.IsCore THEN 'Core' ELSE 'Elective' END AS course_type
    FROM Course c
    JOIN Degree_Course dc ON c.CourseID = dc.CourseID
    JOIN Degree d ON d.DegreeName = dc.DegreeName AND d.DegreeLevel = dc.DegreeLevel
    WHERE d.DegreeName = %s AND d.DegreeLevel = %s;
    """

    # Execute the query with the degree name as parameter
    cursor.execute(query, (Degree_Name,Degree_Level))

    # Fetch all rows
    courses = cursor.fetchall()

    conn.commit()
    conn.close

    if not courses:
        return None
    
    return courses


def Course_Exists(dict_info):
    conn = connect_db()
    cursor = conn.cursor() 
    
    Course_ID = dict_info['courseDeptCode'] + dict_info['courseNum']
    
    # print(f"Course: {Course_ID}")
    # print(f"Course Var Type: {type(Course_ID)}")
    
    # CourseID VARCHAR(8),
    # CourseName VARCHAR(50),
    query = f""" SELECT CourseID 
                FROM Course 
                WHERE CourseID = '{Course_ID}'
            """

    cursor.execute(query)
    rows = cursor.fetchall()
    
    print("**********ROWS IN QUERY RETURNED***********\n",rows)
    if not rows: return False
    
    cursor.close
    conn.close
    
    
    return True

def Section_Exists(dict_info):
    conn = connect_db()
    cursor = conn.cursor() 
    
    Section_ID = dict_info['sectionID']
    Semester = dict_info['semester']
    Year = dict_info['year']
    Course_ID = dict_info['courseDeptCode'] + dict_info['courseNum']
    
    
    # SectionID VARCHAR(3),
    #         Semester VARCHAR(6),
    #         Year INT,
    #         CourseID VARCHAR(8),
    #         NumStudents INT,
    #         InstructorID VARCHAR(8),

    query = f""" SELECT *  
                FROM Section 
                WHERE SectionID = '{Section_ID}' AND
                Semester = '{Semester}' AND
                Year = '{Year}' AND
                CourseID = '{Course_ID}' 
            """

    cursor.execute(query)
    rows = cursor.fetchall()
    
    print("**********ROWS IN QUERY RETURNED***********\n",rows)
    if not rows: return False
    
    cursor.close
    conn.close
    
    return True

def Instructor_Exists(dict_info):
    conn = connect_db()
    cursor = conn.cursor() 
    
    
    InstructorID = dict_info['instructorID']

    query = f""" SELECT *  
                FROM Instructor 
                WHERE InstructorID = '{InstructorID}' 
            """
    cursor.execute(query)
    rows = cursor.fetchall()
    
    print("**********ROWS IN QUERY RETURNED***********\n",rows)
    if not rows: return False
    
    cursor.close
    conn.close
    
    return True

def Degree_Exists(dict_info):
    conn = connect_db()
    cursor = conn.cursor() 
    
    DegreeName = dict_info['name']
    DegreeLevel = dict_info['level']

    query = f""" SELECT *  
                FROM Degree 
                WHERE DegreeName = '{DegreeName}' 
                AND DegreeLevel = '{DegreeLevel}'
            """
            
            
    cursor.execute(query)
    rows = cursor.fetchall()
    
    print("**********ROWS IN QUERY RETURNED***********\n",rows)
    if not rows: return False
    
    cursor.close
    conn.close
    
    return True

def Level_Exists(dict_info):
    conn = connect_db()
    cursor = conn.cursor() 
    
    DegreeLevel = dict_info['levelName']


    query = f""" SELECT *  
                FROM Degree 
                WHERE DegreeLevel = '{DegreeLevel}' 
            """
            
    cursor.execute(query)
    rows = cursor.fetchall()
    
    print("**********ROWS IN QUERY RETURNED***********\n",rows)
    if not rows: return False
    
    cursor.close
    conn.close
    
    return True

