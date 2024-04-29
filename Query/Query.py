from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'oui'  # Add a secret key for flash messages

@app.route('/query')
def home():
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

        # Check if semester ID exists in the Evaluation table:
        semester_id = ''
        if semester == 'Spring':
            semester_id += 'SP'
        elif semester == 'Summer':
            semester_id += 'SU'
        else:
            semester_id += 'FA'
        semester_id += year
        print(semester_id)
        
        # query = "SELECT * FROM Evaluation WHERE SemesterID = %s"
        # cursor.execute(query, (semester_id))

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
