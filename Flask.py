from flask import Flask, render_template, request

app = Flask(__name__)

# 1. Homepage route (GET request by default)
@app.route('/')
def home():
    return render_template('index.html', greeting="Please enter your name below.")

# 2. About route (Independent Practice)
@app.route('/about')
def about():
    return "This is a backend server built for the Girls to Code program."

# 3. Form Handling route (Accepts POST requests)
@app.route('/submit', methods=['POST'])
def submit():
    # Extract the data from the HTML form
    user_name = request.form.get('user_name')
    
    # Create a personalized message
    personalized_greeting = f"Welcome, {user_name}! Your data was processed by Python."
    
    # Render the template again, passing the new greeting
    return render_template('index.html', greeting=personalized_greeting)

if __name__ == '__main__':
    app.run(debug=True)