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
    
    


# @app.route('/add-course', methods=['POST'])
# def Add_Course():
#     return render_template('add-course.html')
    
# @app.route('/add-instructor', methods=['POST'])
# def Add_Instructor():
#     return render_template('add-instructor.html')

# @app.route('/add-section', methods=['POST'])
# def Add_Section():
#     return render_template('add-section.html')

# @app.route('/add-learning-objective', methods=['POST'])
# def Add_LearningObjective():
#     return render_template('add-learning-objective.html')

# @app.route('/add-degree', methods=['GET'])
# def add_degree():
#     return render_template('add_degree.html')

# @app.route('/add-course', methods=['GET'])
# def add_course():
#     return render_template('add_course.html')

# @app.route('/add-instructor', methods=['GET'])
# def add_instructor():
#     return render_template('add_instructor.html')

# @app.route('/add-section', methods=['GET'])
# def add_section():
#     return render_template('add_section.html')

# @app.route('/add-learning-objective', methods=['GET'])
# def add_learning_objective():
#     return render_template('add_learning_objective.html')

# @app.route('/', methods=['GET'])
# def data_entry():
#     return render_template('data_entry.html')

if __name__ == '__main__':
    app.run(debug=True)