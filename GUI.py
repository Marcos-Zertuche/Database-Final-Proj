from flask import Flask, render_template, request, flash, redirect, url_for
from DB_Setup import Insert_Instructor, Insert_Degree, Insert_Level, Insert_Course, Insert_Learning_Objective, connect_db, Check_Course, Insert_Section , Course_Exists , Section_Exists, Instructor_Exists, Degree_Exists , Level_Exists, Insert_Course,Insert_Section, Get_Courses, Check_Instructor, Insert_Evaluation , LO_Exists

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


       
    
@app.route('/enter-evaluation-section', methods = ['POST'])
def Eval_Section(): 
        print(request.form)
        sections = View_(request.form)
        print(sections)
        print(sections[0][0])
        print("hello")
        print(sections[0][1])
        return render_template('./Evaluation/enter-eval-getsection.html', sections = sections)
        
@app.route('/enter-evaluation-LO', methods = ['POST'])
def Eval_LO(): 
        print(request.form)
        return render_template('./Evaluation/enter-eval-getLO.html', sections = sections)

@app.route('/enter-evaluation-info', methods = ['POST'])
def Insert_Eval(): 
         return render_template('./Evaluation/enter-eval-info.html')



@app.route('/submit-eval', methods = ['POST'])
def Submit_Eval(): 
         return render_template('./Evaluation/submit-evaluation.html')


"""CHECK FUNCTIONS:"""
# Return false if it does not meet criteria
def courseCheck(input):
    
    print(input)
    # Check if the input is alphabetical
    if not input['courseDeptCode'].isalpha(): return False

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
    
    if Level_Exists(level_input): return False
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
    print("BREAK HERE")
    if not Course_Exists(input): return False
    
    return True
       
def levelCheck(input):
    if len(input['levelName']) > 5:
        return False
    
    # Check if the val already exists in table
    if Level_Exists(input): return False

    
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


@app.route('/degree-result', methods=['POST'])    
def Degree_Result():
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

        courses = Get_Courses(request.form)

        # # Check if the combination exists in the Degree table:
        # query = "SELECT * FROM Degree WHERE DegreeName = %s AND DegreeLevel = %s"
        # cursor.execute(query, (degree_name, degree_level))

        # # Fetch the result
        # result = cursor.fetchone()

        # conn.close()

        # if result is None:
        #     errors.append("Error: Combination of Degree Name and Level does not exist in the Degree table.")
        
        if errors:
            for error in errors:
                flash(error)
            return render_template('./Degree/list-degree.html')

        # If all checks pass, render the degree-result.html template
        return render_template('./Degree/degree-result.html', courses = courses)


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
            for error in errors:
                flash(error)
            return render_template('./Course/list-course.html')
        
        sections = Check_Course(request.form)
        print(sections)

        # If all checks pass, render the course-result.html template
        return render_template('./Course/course-result.html', sections=sections)


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

        errors = []  # Initialize an empty list to store errors

        # Check if Semester conforms to restrictions (Spring, Summer, Fall)
        if semester not in ['Spring', 'Summer', 'Fall']:
            errors.append("Error: Semester must be Spring, Summer, or Fall.")

        # Check if Year conforms to restrictions (4 characters)
        if len(year) > 4:
            errors.append("Error: Year exceeds 4 characters limit.")

        # # Check if semester ID exists in the Evaluation table:
        # query = "SELECT * FROM Evaluation WHERE Semester = %s AND Year = %s"
        # cursor.execute(query, (semester, year))

        # # Fetch the result
        # result = cursor.fetchone()

        # conn.close()

        # if result is None:
        #     errors.append("Error: Semester ID does not exist in the Evaluation table.")
        
        if errors:
            for error in errors:
                flash(error)
            return render_template('./Evaluation/list-eval.html')

        # If all checks pass, render the eval-result.html template
        return render_template('./Evaluation/eval-result.html')




if __name__ == '__main__':
    app.run(debug=True)