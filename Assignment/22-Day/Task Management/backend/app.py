from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from models import db, Task

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')
    priority = data.get('priority')

    if not title or not priority:
        return jsonify({'error': 'Title and priority are required'}), 400

    task = Task(title=title, priority=priority)
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


@app.route('/tasks', methods=['GET'])
def get_tasks():
    query = Task.query

    priority = request.args.get('priority')
    if priority:
        query = query.filter_by(priority=priority)

    completed = request.args.get('completed')
    if completed is not None and completed != '':
        if completed.lower() == 'true':
            query = query.filter_by(completed=True)
        elif completed.lower() == 'false':
            query = query.filter_by(completed=False)

    tasks = query.order_by(Task.created_at.desc()).all()
    return jsonify([task.to_dict() for task in tasks])


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    task.completed = not task.completed
    db.session.commit()
    return jsonify(task.to_dict())


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
