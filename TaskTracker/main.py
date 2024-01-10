from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load tasks from the JSON file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        tasks = []
    return tasks

# Save tasks to the JSON file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

# Define routes
@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
