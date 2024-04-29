from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/data-entry')
def home():
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
        if not degreeCheck(request.form): return render_template('./Error.html')
        # Degree Name restrictions (alpha char)
        # Combination of Degree Name and Level has to be unique
        # Degree Level has to exist in Level table
        
        return render_template('./Degree/submit-degree.html')
    

@app.route('/add-course', methods=['GET', 'POST'])
def Add_Course():
    # If it's a GET request, render the form for the user to fill out
    return render_template('./Course/add-course-form.html')
    
@app.route('/submit-new-course', methods=[ 'POST'])    
def Submit_Course():
    if request.method == 'POST':
        
        if not courseCheck(request.form): return render_template('./Error.html')

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
    if not input['numStudents'] > 0: return False
    
    
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


if __name__ == '__main__':
    app.run(debug=True)