import mysql.connector
import json
from flask import jsonify


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

def Insert_LO_Course_Association(dict_info):
    conn = connect_db()
    cursor = conn.cursor() 
    
    # print("*****",dict_info) ImmutableMultiDict([('objectiveTitle', 'Final Exam'), ('courseDeptCode', 'CS'), ('courseNum', '4444')])
    
    LearningObjectiveTitle = dict_info['objectiveTitle']
    Course_ID = dict_info["courseDeptCode"] + dict_info["courseNum"]
    
    if LO_Course_Exists(dict_info) : return
    
    cursor.execute("""INSERT INTO LearningObjective_Course(LearningObjectiveTitle, CourseID) VALUES (%s, %s)""", (LearningObjectiveTitle , Course_ID))
    conn.commit()
    
    conn.close
    return

def Insert_Core_Class(dict_info):
    conn = connect_db()
    cursor = conn.cursor() 
    print('-----',dict_info)

    Course_ID  = dict_info["courseDeptCode"] + dict_info["courseNum"]

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
    
    conn.close
    return

def Insert_Learning_Objective(dict_info):
    conn = connect_db()
    cursor = conn.cursor() 

    Objective_Title =  dict_info["objectiveTitle"]
    Description = dict_info["objectiveDescription"]
    Course_ID = dict_info["courseDeptCode"] + dict_info["courseNum"]
    
    
   # Insert into LearningObjective table
    query = """INSERT INTO LearningObjective(ObjectiveTitle, Description) VALUES (%s, %s)"""
    cursor.execute(query, (Objective_Title, Description))
    
    # Insert into LearningObjective_Course table
    query = """INSERT INTO LearningObjective_Course(LearningObjectiveTitle, CourseID) VALUES (%s, %s)"""
    cursor.execute(query, (Objective_Title, Course_ID))
    
    
    conn.commit()
    conn.close
    return

def View_Sections(dict_info):
    conn = connect_db()
    cursor = conn.cursor()

    Instructor_ID = dict_info["instructorID"]
    Semester = dict_info["semester"]
    Year = dict_info["year"]

    query = """
        SELECT CourseID, SectionID
        FROM section
        WHERE InstructorID = %(instructorID)s
        AND Semester = %(semester)s
        AND Year = %(year)s
    """

    print("SQL query:", query)
    print("Instructor_ID:", Instructor_ID)
    print("Semester:", Semester)
    print("Year:", Year)
    cursor.execute(query,{'instructorID': Instructor_ID, 'semester': Semester, 'year': Year})
    sections = cursor.fetchall()
    
    # print("here is sections + {sections}",sections)
    cursor.close()
    conn.close()
    return sections

def View_Objective_Title(dict_info):
    conn = connect_db()
    cursor = conn.cursor()

   
    section = dict_info['section'].split(',')[1]
    course_ID = dict_info['section'].split(',')[0]
    

    query = """
        SELECT LearningObjectiveTitle
        FROM LearningObjective_Course
        WHERE CourseID = %(courseID)s
    """
    cursor.execute(query,{'courseID': course_ID})
    Objective_Title = cursor.fetchall()
    print(Objective_Title)
    return Objective_Title


#  CREATE TABLE IF NOT EXISTS Evaluation (
#             EvalObjective VARCHAR(50),
#             DegreeName VARCHAR(50),
#             DegreeLevel VARCHAR(5),
#             A INT,
#             B INT,
#             C INT,
#             F INT,
#             EvaluationDescription VARCHAR(500),
#             InstructorID VARCHAR(8),
#             SectionID VARCHAR(3),
#             Semester VARCHAR(6),
#             Year INT,
#             CourseID VARCHAR(8),
#             PRIMARY KEY (SectionID, CourseID, EvalObjective), 
#             FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
#             FOREIGN KEY (SectionID, Semester, Year) REFERENCES Section(SectionID, Semester, Year), 
#             FOREIGN KEY (DegreeName, DegreeLevel) REFERENCES Degree(DegreeName, DegreeLevel),
#             FOREIGN KEY (InstructorID) REFERENCES Instructor(InstructorID)
#         );
def Insert_Incomplete_Eval(dict_info):
    # print('INSIDE OF INSERT FUNC' , dict_info)
    conn = connect_db()
    cursor = conn.cursor()
    
    # Eval_Objective = 
    
    query = """ INSERT INTO Evaluation(EvalObjective,DegreeName,DegreeLevel,InstructorID,SectionID,Semester,Year,CourseID ) 
                    VALUES(%s, %s , %s ,%s,%s,%s,%s, %s)
    """
    print(dict_info)
    print(query)
    cursor.execute(query , (dict_info['EvalObjective'], dict_info['DegreeName'] , dict_info['DegreeLevel'] , dict_info['InstructorID'], dict_info['SectionID'], dict_info['Semester'] ,dict_info['Year'] ,dict_info['CourseID']) )

    conn.commit()  # Commit the transaction
    conn.close()   # Close the connection

    return 



def Insert_Evaluation(dict_info):
    conn = connect_db()
    cursor = conn.cursor()

    A = dict_info["Acount"]
    B = dict_info["Bcount"]
    C = dict_info["Ccount"]
    F = dict_info["Fcount"]
    improvements = dict_info["improvementSuggestion"]
    

    query = """INSERT INTO Evaluation(A, B, C, F, EvaluationDescription) VALUES(%s, %s, %s, %s, %s)"""
    cursor.execute(query, (A, B, C, F, improvements))
    
    conn.commit()  # Commit the transaction
    conn.close()   # Close the connection

    # Optionally, you can return a success message or redirect to another page
    return "Evaluation data inserted successfully!"

def Complete_Evaluation(dict_info):
    conn = connect_db()
    cursor = conn.cursor()

    print(dict_info)
    if not Eval_Exists(dict_info) : return 
    
    if dict_info['A'] == None or dict_info['A'] == '' : return

    # query = f"""UPDATE Player
    #             SET Rating = {n_info[9]}
    #             WHERE ID = {n_info[2]}; """

    query = f"""
            UPDATE Evaluation
            SET A = {int(dict_info['A'])} , 
                B = {int(dict_info['B'])} ,
                C = {int(dict_info['C'])} ,
                F = {int(dict_info['F'])} ,
                EvaluationDescription = '{dict_info['EvaluationDescription']}'
            WHERE CourseID = '{dict_info['CourseID']}' AND
                SectionID = '{dict_info['SectionID']}' AND
                EvalObjective = '{dict_info['EvalObjective']}'
    """
    print(query)
    cursor.execute(query)
    conn.commit()  # Commit the transaction
    conn.close()   # Close the connection

    return 


def Get_Courses(dict_info):
     
    conn = connect_db()
    cursor = conn.cursor()

    Degree_Name =  dict_info["name"]
    Degree_Level = dict_info["level"]
    
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

def Get_Sections(dict_info):
    conn = connect_db()
    cursor = conn.cursor()

    print(dict_info)

    Degree_Name =  dict_info["name"]
    Degree_Level = dict_info["level"]
    Start_Semester = dict_info["startSemester"]
    End_Semester = dict_info["endSemester"]
    Start_Year = int(dict_info["startYear"])
    End_Year = int(dict_info["endYear"])

    query = """SELECT s.SectionID, s.courseID, s.Semester, s.Year
    FROM Section s
    JOIN Course c ON s.CourseID = c.CourseID
    JOIN Degree_Course dc ON c.CourseID = dc.CourseID
    JOIN Degree d ON dc.degreeName = d.degreeName AND dc.degreeLevel = d.degreeLevel
    WHERE d.DegreeName = %s
    AND d.DegreeLevel = %s
    AND (s.Year > %s OR (s.Year = %s AND s.Semester >= %s))
    AND (s.Year < %s OR (s.Year = %s AND s.Semester <= %s))
    ORDER BY s.Year, 
         CASE s.Semester 
             WHEN "Spring" THEN 0
             WHEN "Summer" THEN 1
             WHEN "Fall" THEN 2
         END;"""

    cursor.execute(query, (Degree_Name, Degree_Level, Start_Year, Start_Year, Start_Semester, End_Year, End_Year, End_Semester))
    sections = cursor.fetchall()

    conn.commit()
    conn.close()

    if not sections:
        return None

    return sections


def Course_Exists(dict_info):
    conn = connect_db()
    cursor = conn.cursor() 
    
    # dict_info = dict(dict_info1)
    
    print("****" , dict_info)
    
    Course_ID = dict_info['courseDeptCode'] + dict_info['courseNum']
    
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

    print(dict_info)
    
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
                FROM Level 
                WHERE DegreeLevel = '{DegreeLevel}' 
            """
            
    cursor.execute(query)
    rows = cursor.fetchall()
    
    print("**********ROWS IN QUERY RETURNED***********\n",rows)
    if not rows: return False
    
    cursor.close
    conn.close
    
    return True

def LO_Exists(dict_info):
    conn = connect_db()
    cursor = conn.cursor() 
    
    Objective_Title =  dict_info["objectiveTitle"]
    Description = dict_info["objectiveDescription"]
    Course_ID = dict_info['courseDeptCode'] + dict_info['courseNum']
    

    query = f""" SELECT *  
                FROM LearningObjective 
                WHERE ObjectiveTitle = '{Objective_Title}' 
            """
            
    cursor.execute(query)
    rows = cursor.fetchall()
    
    print("**********ROWS IN QUERY RETURNED***********\n",rows)
    if not rows: return False
    
    cursor.close
    conn.close
    
    return True

def LO_Course_Exists(dict_info):
    conn = connect_db()
    cursor = conn.cursor() 
    
    print("*****",dict_info) # ImmutableMultiDict([('objectiveTitle', 'Final Exam'), ('courseDeptCode', 'CS'), ('courseNum', '4444')])
    
    # CREATE TABLE IF NOT EXISTS LearningObjective_Course (
    #         LearningObjectiveTitle VARCHAR(120),
    #         CourseID VARCHAR(8),
    
    LearningObjectiveTitle = dict_info['objectiveTitle']
    Course_ID = dict_info["courseDeptCode"] + dict_info["courseNum"]

    query = f""" SELECT *  
                FROM LearningObjective_Course
                WHERE LearningObjectiveTitle = '{LearningObjectiveTitle}' AND CourseID = '{Course_ID}'
            """
            
    cursor.execute(query)
    rows = cursor.fetchall()
    
    print("**********ROWS IN QUERY RETURNED***********\n",rows)
    if not rows: return False
    
    cursor.close
    conn.close
    
    return True

def Eval_Exists(dict_info):
    conn = connect_db()
    cursor = conn.cursor()
    print('EEEE _----> ',dict_info )
    
    
    if not 'SectionID' in dict_info: return
    
    section_id = dict_info['SectionID']
    course_id = dict_info['CourseID']
    eval_objective = dict_info['EvalObjective']

    query = f"""SELECT COUNT(*) AS EvaluationExists
                FROM Evaluation
                WHERE SectionID = '{section_id}' 
                AND CourseID = '{course_id}'
                AND EvalObjective = '{eval_objective}';
            """
    print(query)
    cursor.execute(query)
    result = cursor.fetchone()

    evaluation_exists = result[0] == 1  # Check if count is 1

    return evaluation_exists


    #if evaluation exists based of primary key

def convert_semester(semester):
    if semester == 'Spring':
        return 0
    elif semester == 'Summer':
        return 1
    else:
        return 2

def Check_Course(dict_info):
    conn = connect_db()
    cursor = conn.cursor()

    Course_ID = dict_info['courseID']
    Start_Semester = convert_semester(dict_info['startSemester'])
    Start_Year = int(dict_info['startYear'])
    End_Semester = convert_semester(dict_info['endSemester'])
    End_Year = int(dict_info['endYear'])

    # Select Sections within the specified semester range
    query = """SELECT * FROM Section WHERE CourseID = %s"""
    cursor.execute(query, (Course_ID,))

    # Fetch all rows
    all_sections = cursor.fetchall()
    print(all_sections)

    sections = []
    for section in all_sections:
        # Extract semester and year from the section
        section_semester = convert_semester(section[1])
        section_year = int(section[2])

        # Check if the section is within the specified semester range
        if (section_year > Start_Year or (section_year == Start_Year and section_semester >= Start_Semester)) \
                and (section_year < End_Year or (section_year == End_Year and section_semester <= End_Semester)):
            sections.append(section)

    conn.close()

    return sections

def Check_Instructor(dict_info):
    conn = connect_db()
    cursor = conn.cursor()

    Instructor_ID = dict_info['instructorID']
    Start_Semester = convert_semester(dict_info['startSemester'])
    Start_Year = int(dict_info['startYear'])
    End_Semester = convert_semester(dict_info['endSemester'])
    End_Year = int(dict_info['endYear'])

    # Select Sections within the specified semester range
    query = """SELECT * FROM Section WHERE InstructorID = %s"""
    cursor.execute(query, (Instructor_ID,))

    # Fetch all rows
    all_sections = cursor.fetchall()
    print(all_sections)

    sections = []
    for section in all_sections:
        # Extract semester and year from the section
        section_semester = convert_semester(section[1])
        section_year = int(section[2])

        # Check if the section is within the specified semester range
        if (section_year > Start_Year or (section_year == Start_Year and section_semester >= Start_Semester)) \
                and (section_year < End_Year or (section_year == End_Year and section_semester <= End_Semester)):
            sections.append(section)

    conn.close()

    return sections

def Get_Objectives(dict_info):
    conn = connect_db()
    cursor = conn.cursor()

    Degree_Name =  dict_info["name"]
    Degree_Level = dict_info["level"]
    
    query = """SELECT CourseID FROM Degree_Course WHERE DegreeName = %s AND DegreeLevel = %s"""
    cursor.execute(query, (Degree_Name,Degree_Level))
    courses = cursor.fetchall()
    print(courses)

    objectives = []
    for course in courses:
        query = """SELECT LearningObjectiveTitle, ObjectiveCode, Description
                    FROM LearningObjective_Course 
                    JOIN LearningObjective ON LearningObjectiveTitle = ObjectiveTitle
                    WHERE CourseID = %s"""
        cursor.execute(query, (course[0],))
        course_objectives = cursor.fetchall()
        print(course_objectives)

        for objective in course_objectives:
            if objective not in objectives:
                objectives.append(objective)

    conn.close
    
    return objectives

def Get_Objective_Course(dict_info):
    conn = connect_db()
    cursor = conn.cursor()

    Degree_Name =  dict_info["name"]
    Degree_Level = dict_info["level"]
    
    query = """SELECT CourseID FROM Degree_Course WHERE DegreeName = %s AND DegreeLevel = %s"""
    cursor.execute(query, (Degree_Name,Degree_Level))
    courses = cursor.fetchall()
    print(courses)

    objectives = {}
    for course in courses:
        query = """SELECT LearningObjectiveTitle FROM LearningObjective_Course WHERE CourseID = %s"""
        cursor.execute(query, (course[0],))
        course_objectives = cursor.fetchall()
        print(course_objectives)

        for objective in course_objectives:
            # Check if the objective already exists in the dictionary
            if objective[0] not in objectives:
                # If it doesn't exist, add it as a key with an empty list
                objectives[objective[0]] = []
            # Append the course ID to the list for this objective key
            if course[0] not in objectives[objective[0]]:
                query = """SELECT CourseName FROM Course WHERE CourseID = %s"""
                cursor.execute(query, (course[0],))
                course_name = cursor.fetchone()
                objectives[objective[0]].append((course[0], course_name[0]))

    print(objectives)

    conn.close
    
    return objectives

def Get_Section_Percentage(dict_info):
    conn = connect_db()
    cursor = conn.cursor()

    Semester = dict_info['semester']
    Year = dict_info['year']
    Percentage = float(dict_info['percentage'])

    query = """SELECT SectionID, A, B, C, F, CourseID FROM Evaluation WHERE Semester = %s AND Year = %s"""
    cursor.execute(query, (Semester, Year))
    selected_sections = cursor.fetchall()
    print(selected_sections)

    sections = []
    for section in selected_sections:
        total_students = section[1] + section[2] + section[3] + section[4]
        passing_percentage = ((section[1] + section[2] + section[3]) / total_students) * 100
        passing_percentage = round(passing_percentage, 2)
        if passing_percentage >= Percentage:
            query = """SELECT * FROM Section WHERE SectionID = %s AND Semester = %s AND Year = %s AND CourseID = %s"""
            cursor.execute(query, (section[0], Semester, Year, section[5]))
            section = cursor.fetchone()
            sections.append((section, passing_percentage))

    return sections


def Get_All_Sections(dict_info):
    semester = dict_info['semester']
    year = dict_info['year']

    conn = connect_db()
    cursor = conn.cursor()

    query = """
        SELECT 
            e.SectionID,
            e.CourseID,
            CASE 
                WHEN e.EvalObjective IS NOT NULL THEN 
                    CASE 
                        WHEN e.A IS NOT NULL OR e.B IS NOT NULL OR e.C IS NOT NULL OR e.F IS NOT NULL THEN 'Entered'
                        ELSE 'Partially Entered'
                    END
                ELSE 'Not Entered'
            END AS EvaluationStatus,
            CASE 
                WHEN e.EvaluationDescription IS NOT NULL AND CHAR_LENGTH(e.EvaluationDescription) > 0 THEN 'Entered'
                ELSE 'Not Entered'
            END AS ImprovementStatus
        FROM 
            Evaluation e
        WHERE 
            e.Semester = %s AND e.Year = %s;
    """

    cursor.execute(query, (semester, year))
    sections_info = cursor.fetchall()

    conn.close()

    return sections_info
