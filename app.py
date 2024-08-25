from flask import Flask, request, jsonify

app = Flask(__name__)

# POST Method
@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    data = request.json.get('data', [])
    user_id = "rithwik_2003"  
    email = "rithwik.21bce9028@vitapstudent.ac.in"
    roll_number = "21BCE9028"

    # Separate numbers and alphabets
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    
    # Find highest lowercase alphabet
    lowercase = [x for x in alphabets if x.islower()]
    highest_lowercase = max(lowercase) if lowercase else None

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
    }

    return jsonify(response)

# GET Method
@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({
        "operation_code": 1
    })

if __name__ == '__main__':
    app.run(debug=True)
