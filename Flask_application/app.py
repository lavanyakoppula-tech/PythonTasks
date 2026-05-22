from flask import Flask, render_template

app = Flask(__name__)

tasks = [
    {"name": "Learn Flask", "status": "Completed"},
    {"name": "Build Todo App", "status": "Not Completed"},
    {"name": "Connect API Later", "status": "Completed"},
    {"name": "HTML Practice", "status": "Not Completed"}
]

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add-task')
def add_task():
    return render_template('add_task.html')

if __name__ == '__main__':
    app.run(debug=True)