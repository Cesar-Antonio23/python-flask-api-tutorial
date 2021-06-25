from flask import Flask, jsonify, request, jsonify

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False}
]

@app.route('/todos', methods=["GET"])
def hello_world():
    json_todos = jsonify(todos)
    return json_todos

    