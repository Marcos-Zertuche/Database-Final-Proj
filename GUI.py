from flask import Flask, render_template, request, flash, redirect, url_for
from DB_Setup import Insert_Instructor

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
        
        print(f"Degree Name: {request.form['name']}")
        print(f"Degree Level: {request.form['level']}")
        
        # Checks to complete 
        if not degreeCheck(request.form) : return render_template('./Error.html')
        # Degree Name restrictions (alpha char)
        # Combination of Degree Name and Level has to be unique
        # Degree Level has to exist in Level table
        
        deg_info = {
            'DegreeName' : request.form['name'] , 
            'DegreeLevel' : request.form['level']
        }
        
        # db.Insert_Degree(deg_info)
        
        return render_template('./Degree/submit-degree.html')
    

@app.route('/add-course', methods=['GET', 'POST'])
def Add_Course():
    # If it's a GET request, render the form for the user to fill out
    return render_template('./Course/add-course-form.html')
    
@app.route('/submit-new-course', methods=[ 'POST'])    
def Submit_Course():
    if request.method == 'POST':
        
        if not courseCheck(request.form) or not sectionCheck(request.form): return render_template('./Error.html')

        return render_template('./Course/submit-course.html')

@app.route('/add-instructor', methods=['GET', 'POST'])
def Add_Instructor():
    # If it's a GET request, render the form for the user to fill out
    return render_template('./Instructor/add-instructor-form.html')
    
@app.route('/submit-new-instructor', methods=[ 'POST'])    
def Submit_Instructor():
    if request.method == 'POST':
        # print(request.form)
        
        # Checks:
        # Instructor ID is numbers and does not exist
        if not instructorCheck(request.form): return render_template('Error.html')
        
        Insert_Instructor(request.form)
        
        # print(f"Instructor ID: {request.form['instructorID']}")
        # print(f"Instructor Name: {request.form['instructorName']}")
        
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
        
        print(f"Section ID: {request.form['sectionID']}")
        # print(f"Course ID: {request.form['courseID']}")
        print(f"Semester: {request.form['semester']}")
        print(f"Year: {request.form['year']}")
        print(f"Instructor ID: {request.form['instructorID']}")
        print(f"Student in Class: {request.form['numStudents']}")
        
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
        
        # Print the form data to the console
        
        if not levelCheck(request.form): return render_template('Error.html')
        return render_template('./Level/submit-level.html')
    
@app.route('/enter-evaluation-init', methods=['GET','POST'])
def Enter_Eval():
        return render_template('./Evaluation/enter-eval-getsection.html')
    
@app.route('/enter-evaluation-section', methods = ['POST'])
def Eval_Section(): 
         return render_template('./Evaluation/enter-eval-getLO.html')
        

@app.route('/enter-evaluation-LO', methods = ['POST'])
def Eval_LO(): 
         return render_template('./Evaluation/enter-eval-info.html')

@app.route('/enter-evaluation-info', methods = ['POST'])
def Insert_Eval(): 
    #return submission complete
         return render_template('./Evaluation/submit-eval.html')



"""CHECK FUNCTIONS:"""
# Return false if it does not meet criteria
def courseCheck(input):
    # Check if the input is alphabetical
    if not input['courseDeptCode'].isalpha(): return False
    
    # Check if input is Shorter than 2 or greater than 4
    if len(input['courseDeptCode']) < 2 or len(input['courseDeptCode']) > 4: return False
    
    # Check if Course Number is 4 digit -> range from 1000 - 9999
    if int(input['courseNum']) < 1000 or int(input['courseNum']) > 9999: return False
    
    # Check if Course Name already exists in DB
    
    
    
    
    # Check if Degree/Level Tuple Exists 
    
    print("Checks passed!")
    return True
    
def degreeCheck(input):
    if len(input['name']) > 50: return False

    # Check if Degree Level conforms to restrictions (DegreeLevel VARCHAR(5))
    if len(input['level']) > 5: return False
        
    # Tuple Does not exist
    
    print("Check Passed!")
    return True

def instructorCheck(input):
    # print(f"Instructor ID: {input['instructorID']}")
    # print(f"Instructor Name: {input['instructorName']}")
    
    # Check if ID is in Instructor table already
    if len(input['instructorName']) > 50:
            return False
    
    # Check if id is valid
    
    print("Check Passed!")
    return True     

def sectionCheck(input):
    # print(input)
    
     # Checks
        # Section does not already exist for that course in that semester in that year
        # Professor exists in instructor table
        # Course exists in course table
        # Semester is either spring summer or fall
        # Year is number and two or four digits depending on what we say
        # Num students is greater than 0 
    # Check section code
    
    # print(section_id)
    
    # Checki if section is valid
    section_id = input['sectionID']
    if  len(section_id) != 3 or not section_id.isdigit(): return False
    
    # Check numstudents greater than 0
    if not int(input['numStudents']) > 0: return False
    
    
    # Check if Course Exists in course table
    
    
    # Do I need degree name/level?
    
    
    
    return True
    
def learnObjCheck(input):
    return True
       
def levelCheck(input):
    if len(input['levelName']) > 5:
        return False
    
    # Check if the val already exists in table
    
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
        print(f"Start Semester: {request.form['startSemester']}")
        print(f"Start Year: {request.form['startYear']}")
        print(f"End Semester: {request.form['endSemester']}")
        print(f"End Year: {request.form['endYear']}")
        
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
        return render_template('./Degree/degree-result.html')


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
        print(f"Course Name: {request.form['courseName']}")
        print(f"Start Semester: {request.form['startSemester']}")
        print(f"Start Year: {request.form['startYear']}")
        print(f"End Semester: {request.form['endSemester']}")
        print(f"End Year: {request.form['endYear']}")
        
        # Get the form data
        course_id = request.form['courseID']
        course_name = request.form['courseName']

        errors = []  # Initialize an empty list to store errors

        # Check if Course ID conforms to restrictions (CourseID VARCHAR(8))
        if len(course_id) > 8:
            errors.append("Error: Course ID exceeds 8 characters limit.")

        # Check if Course Name conforms to restrictions (CourseName VARCHAR(50))
        if len(course_name) > 50:
            errors.append("Error: Course Name exceeds 50 characters limit.")

        # # Check if course ID exists in the Course table:
        # query = "SELECT * FROM Course WHERE CourseID = %s"
        # cursor.execute(query, (course_id))

        # # Fetch the result
        # result = cursor.fetchone()

        # conn.close()

        # if result is None:
        #     errors.append("Error: Course ID does not exist in the Course table.")
        
        if errors:
            for error in errors:
                flash(error)
            return render_template('./Course/list-course.html')

        # If all checks pass, render the course-result.html template
        return render_template('./Course/course-result.html')


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
        print(f"Instructor Name: {request.form['instructorName']}")
        print(f"Start Semester: {request.form['startSemester']}")
        print(f"Start Year: {request.form['startYear']}")
        print(f"End Semester: {request.form['endSemester']}")
        print(f"End Year: {request.form['endYear']}")
        
        # Get the form data
        instructor_id = request.form['instructorID']
        instructor_name = request.form['instructorName']

        errors = []  # Initialize an empty list to store errors

        # Check if Instructor ID conforms to restrictions (InstructorID VARCHAR(8))
        if len(instructor_id) > 8:
            errors.append("Error: Instructor ID exceeds 8 characters limit.")

        # Check if Instructor Name conforms to restrictions (InstructorName VARCHAR(50))
        if len(instructor_name) > 50:
            errors.append("Error: Instructor Name exceeds 50 characters limit.")

        # # Check if instructor ID exists in the Instructor table:
        # query = "SELECT * FROM Instructor WHERE InstructorID = %s"
        # cursor.execute(query, (instructor_id))

        # # Fetch the result
        # result = cursor.fetchone()

        # conn.close()

        # if result is None:
        #     errors.append("Error: Instructor ID does not exist in the Instructor table.")
        
        if errors:
            for error in errors:
                flash(error)
            return render_template('./Instructor/list-instructor.html')

        # If all checks pass, render the instructor-result.html template
        return render_template('./Instructor/instructor-result.html')
    
    
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