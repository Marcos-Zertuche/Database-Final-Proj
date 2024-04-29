from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/query')
def home():
    return render_template('query.html')


@app.route('/list-degree', methods=['GET', 'POST'])
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
        return render_template('./Degree/list-degree.html')


@app.route('/degree-result', methods=[ 'POST'])    
def Submit_Degree():
    if request.method == 'POST':
        print(request.form)
        
        # Print the form data to the console
        
        # You can now use the 'name' and 'email' variables
        # to do whatever you want with the submitted data
        return render_template('./Degree/degree-result.html')
    
    


@app.route('/list-course', methods=['GET', 'POST'])
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
        
        
        return "Course information submitted successfully!"
    else:
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Course/list-course.html')
    
@app.route('/course-result', methods=[ 'POST'])    
def Submit_Course():
    if request.method == 'POST':
        print(request.form)
        
        # Print the form data to the console
        
        # You can now use the 'name' and 'email' variables
        # to do whatever you want with the submitted data
        return render_template('./Course/course-result.html')
    
    

@app.route('/list-instructor', methods=['GET', 'POST'])
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
        
        
        return "Instructor information submitted successfully!"
    else:
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Instructor/list-instructor.html')
    
@app.route('/instructor-result', methods=[ 'POST'])    
def Submit_Instructor():
    if request.method == 'POST':
        print(request.form)
        
        # Print the form data to the console
        
        # You can now use the 'name' and 'email' variables
        # to do whatever you want with the submitted data
        return render_template('./Instructor/instructor-result.html')
    
    
@app.route('/list-eval', methods=['GET', 'POST'])
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
        
        
        return "Evaluation information submitted successfully!"
    else:
        # If it's a GET request, render the form for the user to fill out
        return render_template('./Evaluation/list-eval.html')
    
@app.route('/eval-result', methods=[ 'POST'])    
def Submit_Section():
    if request.method == 'POST':
        print(request.form)
        
        # Print the form data to the console
        
        # You can now use the 'name' and 'email' variables
        # to do whatever you want with the submitted data
        return render_template('./Evaluation/eval-result.html')

if __name__ == '__main__':
    app.run(debug=True)
