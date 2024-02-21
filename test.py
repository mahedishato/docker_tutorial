from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)





@app.route('/', methods=['POST'])
def hash_password():
    data = request.form['password'].lower()
    password = data.encode('utf-8')
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    hashed_password= hashed_password.lower()

    return hashed_password

@app.route('/new', methods = ['POST'])
def input():
    mahedi = request.form['name']
    mahedi = mahedi.upper()

    return mahedi


@app.route('/math', methods=["POST"])
def math():
    first = int(request.form['first'])
    second = int(request.form['second'])
    result = first + second

    return str(result)





if __name__ == '__main__':
    app.run(debug=True)