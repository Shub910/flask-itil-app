from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def welcome():
    return "Welcome to ITIL exam"
@app.route('/modules')
def modules():
    # Replace the following list with the actual DITISS module names
    module_names = [
        "Module 1: Introduction to ITIL",
        "Module 2: Service Management",
        "Module 3: Service Design",
        "Module 4: Service Transition",
        "Module 5: Service Operation",
        "Module 6: Continual Service Improvement"
    ]
    return jsonify(module_names)

@app.route('/me')
def me():
    # Replace these details with your actual information
    info = {
        "PRN": "240344223018",
        "Name": "Shubham",
        "Phone Number": "9067971110"
    }
    return jsonify(info)

if __name__ == '__main__':
    app.run(debug=True)
