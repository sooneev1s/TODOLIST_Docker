# app/routes.py
from flask import request, jsonify
from app import app, db
from app.models import Todo

@app.route('/todos', methods=['POST'])
def create_todo():
    title = request.json['title']
    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({"id": new_todo.id, "title": new_todo.title})

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([{"id": todo.id, "title": todo.title} for todo in todos])
