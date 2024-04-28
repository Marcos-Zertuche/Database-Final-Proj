from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/data-entry')
def home():
    return render_template('data-entry.html')


@app.route('/add-degree', methods=['GET', 'POST'])
def Add_Degree():
    if request.method == 'POST':
        # Process the submitted form data
        # Access the submitted data using request.form['input_name']
        # For example: degree_name = request.form['degree_name']
        # Perform any necessary processing with the submitted data
        # Then you can redirect to another page or render a template
        
        # For now, let's just print the submitted data
        print(request.form)
        
        """Error checking, break out for adding to table"""
        
        
        return "Degree information submitted successfully!"
    else:
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Degree/add-degree-form.html')


@app.route('/submit-new-degree', methods=[ 'POST'])    
def Submit_Degree():
    if request.method == 'POST':
        print(request.form)
        
        # Print the form data to the console
        
        # You can now use the 'name' and 'email' variables
        # to do whatever you want with the submitted data
        return render_template('./Degree/submit-degree.html')
    
    


@app.route('/add-course', methods=['GET', 'POST'])
def Add_Course():
    if request.method == 'POST':
        # Process the submitted form data
        # Access the submitted data using request.form['input_name']
        # For example: degree_name = request.form['degree_name']
        # Perform any necessary processing with the submitted data
        # Then you can redirect to another page or render a template
        
        # For now, let's just print the submitted data
        print(request.form)
        
        """Error checking, break out for adding to table"""
        
        
        return "Degree information submitted successfully!"
    else:
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Course/add-course-form.html')
    
@app.route('/submit-new-course', methods=[ 'POST'])    
def Submit_Course():
    if request.method == 'POST':
        print(request.form)
        
        # Print the form data to the console
        
        # You can now use the 'name' and 'email' variables
        # to do whatever you want with the submitted data
        return render_template('./Course/submit-course.html')
    
    

@app.route('/add-instructor', methods=['GET', 'POST'])
def Add_Instructor():
    if request.method == 'POST':
        # Process the submitted form data
        # Access the submitted data using request.form['input_name']
        # For example: degree_name = request.form['degree_name']
        # Perform any necessary processing with the submitted data
        # Then you can redirect to another page or render a template
        
        # For now, let's just print the submitted data
        print(request.form)
        
        """Error checking, break out for adding to table"""
        
        
        return "Degree information submitted successfully!"
    else:
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Instructor/add-instructor-form.html')
    
@app.route('/submit-new-instructor', methods=[ 'POST'])    
def Submit_Instructor():
    if request.method == 'POST':
        print(request.form)
        
        # Print the form data to the console
        
        # You can now use the 'name' and 'email' variables
        # to do whatever you want with the submitted data
        return render_template('./Instructor/submit-instructor.html')
    
    
@app.route('/add-section', methods=['GET', 'POST'])
def Add_Section():
    if request.method == 'POST':
        # Process the submitted form data
        # Access the submitted data using request.form['input_name']
        # For example: degree_name = request.form['degree_name']
        # Perform any necessary processing with the submitted data
        # Then you can redirect to another page or render a template
        
        # For now, let's just print the submitted data
        print(request.form)
        
        """Error checking, break out for adding to table"""
        
        
        return "Degree information submitted successfully!"
    else:
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Section/add-section-form.html')
    
@app.route('/submit-new-section', methods=[ 'POST'])    
def Submit_Section():
    if request.method == 'POST':
        print(request.form)
        
        # Print the form data to the console
        
        # You can now use the 'name' and 'email' variables
        # to do whatever you want with the submitted data
        return render_template('./Section/submit-section.html')

@app.route('/add-learning-objective', methods=['GET', 'POST'])
def Add_LearnObj():
    if request.method == 'POST':
        # Process the submitted form data
        # Access the submitted data using request.form['input_name']
        # For example: degree_name = request.form['degree_name']
        # Perform any necessary processing with the submitted data
        # Then you can redirect to another page or render a template
        
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