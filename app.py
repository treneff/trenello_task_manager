from flask import Flask, render_template
from controllers.task_controller import tasks_blueprint
from controllers.project_controller import projects_blueprint
app = Flask(__name__)

app.register_blueprint(tasks_blueprint)
app.register_blueprint(projects_blueprint)

@app.route('/')
def home():
    return 'Hey'

if __name__ == '__main__':
    app.run(debug=True)