from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


todo = (
    {
    'id': 1,
    'title': 'Buy milk',
    'isComplited': False,
    'deadline': '01.11.22', 
    },
    {
    'id': 2,
    'title': 'Buy water',
    'isComplited': False,
    'deadline': '05.11.22',
    },
    {
    'id': 3,
    'title': 'Buy dog',
    'isComplited': False,
    'deadline': '10.11.22',
    })

@app.route('/')
def home_page():
    return '<h1> Write in URL " /todos", Hrundel!=) </h1>'

@app.route('/todos', methods=['GET'])
def get_todo():
    return jsonify(todo)




if __name__ == '__main__':
    app.run(debug=True)