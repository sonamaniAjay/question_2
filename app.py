from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['post'])
def login():
    user_id = request.form['userId']
    password = request.form['password']

    if user_id == 'ajay_sonwani_2904' and password == '230001004':
        return 'Login successful!'
    else:
        return 'Login failed!'

if __name__ == '__main__':
    app.run(debug=True)
