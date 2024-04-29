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
        # Degree Name restrictions (alpha char)
        # Degree Level has to exist in Level table
        
        return render_template('./Degree/submit-degree.html')
    

@app.route('/add-course', methods=['GET', 'POST'])
def Add_Course():
    # If it's a GET request, render the form for the user to fill out
    return render_template('./Course/add-course-form.html')
    
@app.route('/submit-new-course', methods=[ 'POST'])    
def Submit_Course():
    if request.method == 'POST':
        print(request.form)
        
        # Checks to complete 
        # CourseID does not exist
        # Course ID follows defined format
        # DegreeName, DegreeLevel tuple Exists 

        
        print(f"courseID: {request.form['courseID']}")
        print(f"courseName: {request.form['courseName']}")
        print(f"degreeName: {request.form['degreeName']}")
        print(f"degreeLevel: {request.form['degreeLevel']}")

        
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
        # Instructor Name is alpha chars
        
        print(f"Instructor ID: {request.form['instructorID']}")
        print(f"Instructor Name: {request.form['instructorName']}")
        
        return render_template('./Instructor/submit-instructor.html')
    
    
@app.route('/add-section', methods=['GET', 'POST'])
def Add_Section():
    # If it's a GET request, render the form for the user to fill out
    return render_template('./Section/add-section-form.html')
    
@app.route('/submit-new-section', methods=[ 'POST'])    
def Submit_Section():
    if request.method == 'POST':
        print(request.form)
        
        # Checks
        # Section does not already exist for that course in that semester in that year
        # Professor exists in instructor table
        # Course exists in course table
        # Semester is either spring summer or fall
        # Year is number and two or four digits depending on what we say
        # Num students is greater than 0 
        
        
        print(f"Section ID: {request.form['sectionID']}")
        print(f"Course ID: {request.form['courseID']}")
        print(f"Semester: {request.form['semester']}")
        print(f"Year: {request.form['year']}")
        print(f"Instructor ID: {request.form['instructorID']}")
        print(f"Student in Class: {request.form['numStudents']}")
        
        return render_template('./Section/submit-section.html')

@app.route('/add-learning-objective', methods=['GET', 'POST'])
def Add_LearnObj():
    if request.method == 'POST':
        
        # For now, let's just print the submitted data
        print(request.form)
        
        """Error checking, break out for adding to table"""
        
        
        return "Degree information submitted successfully!"
    else:
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Learning-Objective/add-lo-form.html')
    
@app.route('/submit-new-learning-objective', methods=[ 'POST'])    
def Submit_LearnObj():
    if request.method == 'POST':
        print(request.form)
        
        # Print the form data to the console
        
        # You can now use the 'name' and 'email' variables
        # to do whatever you want with the submitted data
        return render_template('./Learning-Objective/submit-lo.html')

# @app.route('/add-learning-objective', methods=['POST'])
# def Add_LearningObjective():
#     return render_template('add-learning-objective.html')

if __name__ == '__main__':
    app.run(debug=True)