from flask import Flask # type: ignore
from flask_cors import CORS # type: ignore

app= Flask(__name__)
cors = CORS(app, origins='*') # enable CORS on all routes

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/users')
def get_users():
    return {
        'users': [
            {
                'id': 1,
                'first_name': 'Dave',
                'last_name': 'Jhonson'
            }, {
                'id': 2,
                'first_name': 'Alice',
                'last_name': 'Miller'
            }, {
                'id': 3,
                'first_name': 'Mellissa',
                'last_name': 'Clark'
            }  
        ]
    }

@app.route('/api/fruits')
def get_fruits():
    return {
        'fruits': ['Apple', 'Banana', 'Cherry' ]
    }

if __name__ == '__main__':
    app.run(debug=True, port=8080) # by default, Flask runs on port 5000

