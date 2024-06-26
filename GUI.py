from flask import Flask, render_template, request, flash, redirect, url_for

from DB_Setup import Insert_Instructor, Insert_Degree, Insert_Level, Insert_Course, Insert_Learning_Objective, connect_db, Check_Course, Insert_Section , Course_Exists , Section_Exists, Instructor_Exists, Degree_Exists , Level_Exists, Insert_Course,Insert_Section, Get_Courses, Check_Instructor, View_Sections, LO_Exists, View_Objective_Title, Insert_Evaluation,Insert_Core_Class, Insert_LO_Course_Association, LO_Course_Exists, Get_Objectives, Get_Objective_Course, Get_Sections, Insert_Incomplete_Eval, Get_Section_Percentage, Get_All_Sections, Get_Sections, Complete_Evaluation


app = Flask(__name__)
app.secret_key = 'oui'  # Add a secret key for flash messages

@app.route('/')
def home():
    return render_template('home.html')


# """MARCOS ORIGINAL CODE"""
@app.route('/data-entry')
def Data_Entry():
    return render_template('data-entry.html')


@app.route('/add-degree', methods=['GET', 'POST'])
def Add_Degree():
    # If it's a GET request, render the form for the user to fill out
    return render_template('./Degree/add-degree-form.html')

@app.route('/submit-new-degree', methods=[ 'POST'])    
def Submit_Degree():
    if request.method == 'POST':
        print(request.form)
        
        # Checks to complete 
        if not degreeCheck(request.form) : return render_template('./Error.html')
        
        Insert_Degree(request.form)
              
        return render_template('./Degree/submit-degree.html')

@app.route('/add-course', methods=['GET', 'POST'])
def Add_Course():
    # If it's a GET request, render the form for the user to fill out
    return render_template('./Course/add-course-form.html')
    
@app.route('/submit-new-course', methods=[ 'POST'])    
def Submit_Course():
    if request.method == 'POST':
        
        if not courseCheck(request.form) : return render_template('./Error.html')
        Insert_Course(request.form)
        return render_template('./Course/submit-course.html')

@app.route('/add-instructor', methods=['GET', 'POST'])
def Add_Instructor():
    # If it's a GET request, render the form for the user to fill out
    return render_template('./Instructor/add-instructor-form.html')
    
@app.route('/submit-new-instructor', methods=[ 'POST'])    
def Submit_Instructor():
    if request.method == 'POST':
        if not instructorCheck(request.form): return render_template('Error.html')
        
        Insert_Instructor(request.form)
        
        return render_template('./Instructor/submit-instructor.html')
    
    
@app.route('/add-section', methods=['GET', 'POST'])
def Add_Section():
    # If it's a GET request, render the form for the user to fill out
    return render_template('./Section/add-section-form.html')
    
@app.route('/submit-new-section', methods=[ 'POST'])    
def Submit_Section():
    if request.method == 'POST':
        print(request.form)
        
        if not sectionCheck(request.form): return render_template('Error.html')
        
        Insert_Section(request.form)
        
        return render_template('./Section/submit-section.html')


@app.route('/add-learning-objective', methods=['GET', 'POST'])
def Add_LearnObj():
        return render_template('./Learning-Objective/add-lo-form.html')
    
@app.route('/submit-new-learning-objective', methods=[ 'POST'])    
def Submit_LearnObj():
    if request.method == 'POST':
        print(request.form)
        # Print the form data to the console
        if not learnObjCheck(request.form): return render_template('Error.html')
        
        Insert_Learning_Objective(request.form)
        # You can now use the 'name' and 'email' variables
        # to do whatever you want with the submitted data
        return render_template('./Learning-Objective/submit-lo.html')

@app.route('/add-level', methods=['GET', 'POST'])
def Add_Level():
        return render_template('./Level/add-level-form.html')
    
@app.route('/submit-new-level', methods=[ 'POST'])    
def Submit_Level():
    if request.method == 'POST':
        print(request.form)
        
        if not levelCheck(request.form): return render_template('Error.html')
        
        Insert_Level(request.form)
        return render_template('./Level/submit-level.html')

@app.route('/enter-evaluation-init', methods=['GET','POST'])
def Enter_Eval():
        return render_template('./Evaluation/enter-eval-initial.html')


EVAL_DICT = {}

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

@app.route('/enter-evaluation-section', methods = ['POST'])
def Eval_Section(): 
        print(request.form)
        global EVAL_DICT
        
        sections = View_Sections(request.form)
        print("SECTIONS:" , sections)
        EVAL_DICT['DegreeName'] = request.form['degree']
        EVAL_DICT['DegreeLevel'] = request.form['deg_level']
        EVAL_DICT['Semester'] = request.form['semester']
        EVAL_DICT['Year'] = request.form['year']
        EVAL_DICT['InstructorID'] = request.form['instructorID']
        print(EVAL_DICT)
        return render_template('./Evaluation/enter-eval-getsection.html', sections = sections)

        
@app.route('/enter-evaluation-LO', methods = ['POST'])
def Eval_LO(): 
        global EVAL_DICT
        print(EVAL_DICT)
        print(request.form)
        
        
        # Parse out course ID and Section ID
        parts = request.form['section'].split(',')
        
        EVAL_DICT['CourseID'] = parts[0]
        EVAL_DICT['SectionID'] = parts[1]
         
         
        print(EVAL_DICT)
        
        objectivetitles= View_Objective_Title(request.form)
        print("OBJECTIVES", objectivetitles)
        return render_template('./Evaluation/enter-eval-getLO.html', objectivetitles = objectivetitles )

@app.route('/enter-evaluation-info', methods = ['POST'])
def Insert_Eval(): 
        global EVAL_DICT
        print(request.form)
        EVAL_DICT['EvalObjective'] = request.form['objectivetitles'].split(',')[0].strip("('") 
        print('******', EVAL_DICT)
        
        Insert_Incomplete_Eval(EVAL_DICT)
        
        return render_template('./Evaluation/enter-eval-info.html')



@app.route('/submit-eval', methods = ['POST'])
def Submit_Eval(): 
        global EVAL_DICT
        print(request.form)
        EVAL_DICT['A'] = request.form['Acount']
        EVAL_DICT['B'] = request.form['Bcount']
        EVAL_DICT['C'] = request.form['Ccount']
        EVAL_DICT['F'] = request.form['Fcount']
        EVAL_DICT['EvaluationDescription'] = request.form['improvementSuggestion']
         
        Complete_Evaluation(EVAL_DICT)
        #return submission complete
        return render_template('./Evaluation/submit-evaluation.html')

@app.route('/associate-lo-course' , methods=['GET', 'POST'])
def Insert_LO_Course_Assoc():
    return render_template('./LO-Course/assoc-lo-course.html')

@app.route('/submit-lo-course-association' , methods=['GET', 'POST'])
def Submit_Assoc():
    if request.method == 'POST':
        print(request.form)
        if not assocCheck(request.form) : return render_template('Error.html')
        
        # FUNCTION NEEDED HERE
        Insert_LO_Course_Association(request.form)
        
        
        return render_template('./LO-Course/submit-assoc.html')

@app.route('/assign-core' , methods=['GET', 'POST'])
def Insert_Core():
    return render_template('./Core-Course/designate-core.html')

@app.route('/submit-core' , methods=['GET', 'POST'])
def Submit_Core():
    if request.method == 'POST':
        print(request.form)
        if not coreCheck(request.form): return render_template('Error.html') 
        Insert_Core_Class(request.form)
        return render_template('./Core-Course/submit-core.html')




"""CHECK FUNCTIONS:"""
# Return false if it does not meet criteria
def courseCheck(input):
    
    print(input)
    # Check if the input is alphabetical
    if not input['courseDeptCode'].isalpha(): return False

       # Check numstudents greater than 0
    if not int(input['numStudents']) > 0: return False

    # Check if input is Shorter than 2 or greater than 4
    if len(input['courseDeptCode']) < 2 or len(input['courseDeptCode']) > 4: return False

    # Check if Course Number is 4 digit -> range from 1000 - 9999
    if int(input['courseNum']) < 1000 or int(input['courseNum']) > 9999: return False

    # Check if Course Name already exists in DB
    if Course_Exists(input): return False
    # if not sectionCheck(input): return False 
    
    print("Checks passed!")
    return True
    
def degreeCheck(input):
    if len(input['name']) > 50: return False

    # Check if Degree Level conforms to restrictions (DegreeLevel VARCHAR(5))
    if len(input['level']) > 5: return False

    # If level does not exist
    level_input = { 'levelName' : input['level'] }
    
    if not Level_Exists(level_input): return False
    # Tuple exist
    if Degree_Exists(input): return False

    
    print("Check Passed!")
    return True

def instructorCheck(input):
    if len(input['instructorName']) > 50:
            return False
    
    # Check if id is valid
    if Instructor_Exists(input): return False
        
    
    print("Check Passed!")
    return True     

def sectionCheck(input):
    # Checki if section is valid
    section_id = input['sectionID']
    if  len(section_id) != 3 or not section_id.isdigit(): return False
    
    # Check numstudents greater than 0
    if not int(input['numStudents']) > 0: return False
    
    # Check if section exists
    if Section_Exists(input): return False
    
    # Check if Course Exists in course table
    if not Course_Exists(input) : return False
    
    # Check if 
    if not Instructor_Exists(input): return False
    
    return True
    
def learnObjCheck(input):
    
    print(input)
    if LO_Exists(input) : return False

    if not Course_Exists(input): return False
    
    return True
       
def levelCheck(input):
    if len(input['levelName']) > 5:
        return False
    
    # Check if the val already exists in table
    if Level_Exists(input): return False

    
    return True
def coreCheck(input):
    # Check if Course Exists and Degree Exists
    print("______>>>>>",input)
    if not Course_Exists(input): return False
    
    deg_dict = {
        'name' : input['degreeName'],
        'level' : input['degreeLevel']
    }
    if not Degree_Exists(deg_dict): return False
    
    return True
    
    
    

def assocCheck(input) : 
    #Check if Objective and CourseExists
    print(input)
    
    
    # Objective_Title =  dict_info["objectiveTitle"]
    # Description = dict_info["objectiveDescription"]
    # Course_ID = dict_info["courseDeptCode"] + dict_info['courseNum']
    
    lo_dict = {
        'objectiveTitle' : input['objectiveTitle'],
        'objectiveDescription' : '', 
        'courseDeptCode' : input["courseDeptCode"],
        'courseNum' : input["courseNum"]
    }
    # print(lo_dict)
    if not LO_Exists(lo_dict): return False
    print("BREAK HERE")
    if not Course_Exists(input): return False
    print("BREAK HERE")
    
    # LearningObjectiveTitle = input['objectiveTitle']
    # Course_ID = dict_info["courseDeptCode"] + dict_info["courseNum"]
    
    if LO_Course_Exists(lo_dict): return False
    print("BREAK HERE")
    
    return True

#""" ERIC ORIGINAL CODE"""

@app.route('/query')
def Query():
    return render_template('query.html')


@app.route('/list-degree', methods=['GET'])
def List_Degree():
    if request.method == 'GET':
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Degree/list-degree.html')
    
@app.route('/list-section', methods=['GET'])
def List_Section():
    if request.method == 'GET':
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Degree/list-sections-given-deg.html')


@app.route('/degree-result', methods=['POST'])    
def Degree_Result():
    if request.method == 'POST':
        # Print the form data to the console
        print(request.form)
        
        # Get the form data
        degree_name = request.form['name']
        degree_level = request.form['level']

        errors = []  # Initialize an empty list to store errors

        # Check if Degree Name conforms to restrictions (DegreeName VARCHAR(50))
        if len(degree_name) > 50:
            errors.append("Error: Degree Name exceeds 50 characters limit.")

        # Check if Degree Level conforms to restrictions (DegreeLevel VARCHAR(5))
        if len(degree_level) > 5:
            errors.append("Error: Degree Level exceeds 5 characters limit.")

        # Check if the combination exists in the Degree table:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM Degree WHERE DegreeName = %s AND DegreeLevel = %s"
        cursor.execute(query, (degree_name, degree_level))

        # Fetch the result
        result = cursor.fetchone()

        conn.close()

        if result is None:
            errors.append("Error: Combination of Degree Name and Level does not exist in the Degree table.")
        
        if errors:
            for error in errors:
                flash(error)
            return render_template('./Degree/list-degree.html')
        
        courses = Get_Courses(request.form)

        # If all checks pass, render the degree-result.html template
        return render_template('./Degree/degree-result.html', courses = courses)

@app.route('/list-objectives', methods=['GET'])
def List_Objectives():
    if request.method == 'GET':
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Learning-Objective/list-objectives.html')


@app.route('/objectives-result', methods=['POST'])    
def Objectives_Result():
    if request.method == 'POST':
        # Print the form data to the console
        print(request.form)
        print(f"Degree Name: {request.form['name']}")
        print(f"Degree Level: {request.form['level']}")
        
        # Get the form data
        degree_name = request.form['name']
        degree_level = request.form['level']

        errors = []  # Initialize an empty list to store errors

        # Check if Degree Name conforms to restrictions (DegreeName VARCHAR(50))
        if len(degree_name) > 50:
            errors.append("Error: Degree Name exceeds 50 characters limit.")

        # Check if Degree Level conforms to restrictions (DegreeLevel VARCHAR(5))
        if len(degree_level) > 5:
            errors.append("Error: Degree Level exceeds 5 characters limit.")

        # Check if the combination exists in the Degree table:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM Degree WHERE DegreeName = %s AND DegreeLevel = %s"
        cursor.execute(query, (degree_name, degree_level))

        # Fetch the result
        result = cursor.fetchone()

        conn.close()

        if result is None:
            errors.append("Error: Combination of Degree Name and Level does not exist in the Degree table.")
        
        if errors:
            for error in errors:
                flash(error)
            return render_template('./Learning-Objective/list-objectives.html')
        
        objectives = Get_Objectives(request.form)

        # If all checks pass, render the objectives-result.html template
        return render_template('./Learning-Objective/objectives-result.html', objectives = objectives)


@app.route('/list-objective-course', methods=['GET'])
def List_Objective_Course():
    if request.method == 'GET':
        # If it's a GET request, render the form for the user to fill out
        return render_template('./LO-Course/list-objective-course.html')
    

@app.route('/objective-course-result', methods=['POST'])    
def Objective_Course_Result():
    if request.method == 'POST':
        # Print the form data to the console
        print(request.form)
        print(f"Degree Name: {request.form['name']}")
        print(f"Degree Level: {request.form['level']}")
        
        # Get the form data
        degree_name = request.form['name']
        degree_level = request.form['level']

        errors = []  # Initialize an empty list to store errors

        # Check if Degree Name conforms to restrictions (DegreeName VARCHAR(50))
        if len(degree_name) > 50:
            errors.append("Error: Degree Name exceeds 50 characters limit.")

        # Check if Degree Level conforms to restrictions (DegreeLevel VARCHAR(5))
        if len(degree_level) > 5:
            errors.append("Error: Degree Level exceeds 5 characters limit.")

        # Check if the combination exists in the Degree table:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM Degree WHERE DegreeName = %s AND DegreeLevel = %s"
        cursor.execute(query, (degree_name, degree_level))

        # Fetch the result
        result = cursor.fetchone()

        conn.close()

        if result is None:
            errors.append("Error: Combination of Degree Name and Level does not exist in the Degree table.")
        
        if errors:
            for error in errors:
                flash(error)
            return render_template('./LO-Course/list-objective-course.html')
        
        objective_courses = Get_Objective_Course(request.form)
        print(objective_courses)

        # If all checks pass, render the objective-course-result.html template
        return render_template('./LO-Course/objective-course-result.html', objective_courses = objective_courses)


@app.route('/list-course', methods=['GET'])
def List_Course():
    if request.method == 'GET':
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Course/list-course.html')
    

@app.route('/course-result', methods=['POST'])    
def Course_Result():
    if request.method == 'POST':
        # Print the form data to the console
        print(request.form)
        print(f"Course ID: {request.form['courseID']}")
        print(f"Start Semester: {request.form['startSemester']}")
        print(f"Start Year: {request.form['startYear']}")
        print(f"End Semester: {request.form['endSemester']}")
        print(f"End Year: {request.form['endYear']}")
        
        # Get the form data
        course_id = request.form['courseID']

        errors = []  # Initialize an empty list to store errors

        # Check if Course ID conforms to restrictions (CourseID VARCHAR(8))
        if len(course_id) > 8:
            errors.append("Error: Course ID exceeds 8 characters limit.")

        # Check if course ID exists in the Course table:
        conn = connect_db()
        cursor = conn.cursor()
        query = """SELECT * FROM Course WHERE CourseID = %s"""
        cursor.execute(query, (course_id,))

        # Fetch the result
        result = cursor.fetchone()

        conn.close()

        if result is None:
            errors.append("Error: Course ID does not exist in the Course table.")
        
        if errors:
            return render_template('./Course/list-course.html')
        
        sections = Check_Course(request.form)
        print(sections)

        # If all checks pass, render the course-result.html template
        return render_template('./Course/course-result.html', sections=sections)

@app.route('/section-result', methods=['POST'])    
def Section_Result():
        # Get the form data
        degree_name = request.form['name']
        degree_level = request.form['level']

        errors = []  # Initialize an empty list to store errors

        # Check if Degree Name conforms to restrictions (DegreeName VARCHAR(50))
        if len(degree_name) > 50:
            errors.append("Error: Degree Name exceeds 50 characters limit.")

        # Check if Degree Level conforms to restrictions (DegreeLevel VARCHAR(5))
        if len(degree_level) > 5:
            errors.append("Error: Degree Level exceeds 5 characters limit.")
        
        if errors:
            for error in errors:
                flash(error)
            return render_template('./Degree/section-result.html')
        
        sections = Get_Sections(request.form)
        print(sections)

        # If all checks pass, render the course-result.html template
        return render_template('./Degree/section-result.html', sections=sections)
    
@app.route('/list-instructor', methods=['GET'])
def List_Instructor():
    if request.method == 'GET':
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Instructor/list-instructor.html')
    

@app.route('/instructor-result', methods=['POST'])    
def Instructor_Result():
    if request.method == 'POST':
        # Print the form data to the console
        print(request.form)
        print(f"Instructor ID: {request.form['instructorID']}")
        print(f"Start Semester: {request.form['startSemester']}")
        print(f"Start Year: {request.form['startYear']}")
        print(f"End Semester: {request.form['endSemester']}")
        print(f"End Year: {request.form['endYear']}")
        
        # Get the form data
        instructor_id = request.form['instructorID']

        errors = []  # Initialize an empty list to store errors

        # Check if Instructor ID conforms to restrictions (InstructorID VARCHAR(8))
        if len(instructor_id) > 8:
            errors.append("Error: Instructor ID exceeds 8 characters limit.")

        # Check if instructor ID exists in the Instructor table:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM Instructor WHERE InstructorID = %s"
        cursor.execute(query, (instructor_id,))

        # Fetch the result
        result = cursor.fetchone()

        conn.close()

        if result is None:
            errors.append("Error: Instructor ID does not exist in the Instructor table.")
        
        if errors:
            for error in errors:
                flash(error)
            return render_template('./Instructor/list-instructor.html')
        
        sections = Check_Instructor(request.form)
        print(sections)

        # If all checks pass, render the instructor-result.html template
        return render_template('./Instructor/instructor-result.html', sections=sections)
    
    
@app.route('/list-eval', methods=['GET'])
def List_Evaluation():
    if request.method == 'GET':
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Evaluation/list-eval.html')

    
@app.route('/eval-result', methods=['POST'])    
def Evaluation_Result():
    if request.method == 'POST':
        # Print the form data to the console
        print(request.form)
        print(f"Semester: {request.form['semester']}")
        print(f"Year: {request.form['year']}")
        print(f"Percentage: {request.form['percentage']}")
        
        # Get the form data
        semester = request.form['semester']
        year = request.form['year']
        percentage = request.form['percentage']

        errors = []  # Initialize an empty list to store errors

        # Check if Semester conforms to restrictions (Spring, Summer, Fall)
        # if semester not in ['Spring', 'Summer', 'Fall']:
        #     errors.append("Error: Semester must be Spring, Summer, or Fall.")

        # Check if Year conforms to restrictions (4 characters)
        if len(year) > 4:
            errors.append("Error: Year exceeds 4 characters limit.")

        # Check if semester plus year exists in the Evaluation table:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM Evaluation WHERE Semester = %s AND Year = %s"
        cursor.execute(query, (semester, year))

        # Fetch the result
        result = cursor.fetchone()

        conn.close()

        if result is None:
            errors.append("Error: Semester, Year combination does not exist in the Evaluation table.")
        
        if errors:
            for error in errors:
                flash(error)
            return render_template('./Evaluation/list-eval.html')
        
        sections = Get_Section_Percentage(request.form)

        # If all checks pass, render the eval-result.html template
        return render_template('./Evaluation/eval-result.html', sections=sections, percentage=percentage)

@app.route('/list-eval-submitted' , methods =['GET', 'POST'] )
def Eval_Completion():
    return render_template('./Evaluation/list-eval-submitted.html')
    
@app.route('/eval-submitted-result' , methods =['GET', 'POST'] )
def Eval_Sections_Results():
    print(request.form)
    sections = Get_All_Sections(request.form)
    return render_template('./Evaluation/eval-submitted-results.html' , sections=sections)
    
if __name__ == '__main__':
    app.run(debug=True)