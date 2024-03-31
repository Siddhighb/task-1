from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Route for the calculator page
@app.route('/')
def calculator():
    return render_template('calculator.html')

# Route for the calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operator = request.form['operator']
    result = None
    error_message = None

    if num1.isdigit() and num2.isdigit():
        num1 = float(num1)
        num2 = float(num2)
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                error_message = "Cannot divide by zero!"
        return render_template('calculator.html', result=result, num1=num1, num2=num2, operator=operator, error_message=error_message)
    else:
        error_message = "Invalid input! Please enter numeric values."
        return render_template('calculator.html', error_message=error_message)

# Route for the goodbye page
@app.route('/goodbye')
def goodbye():
    return render_template('goodbye.html')

if __name__ == '__main__':
    app.run(debug=True)
