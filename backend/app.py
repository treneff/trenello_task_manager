from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from controllers.task_controller import tasks_blueprint
from controllers.project_controller import projects_blueprint

app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://trenello_task_manager.db"
db.init_app(app)

app.register_blueprint(tasks_blueprint)
app.register_blueprint(projects_blueprint)

@app.route('/')
def home():
    return "hey"

if __name__ == '__main__':
    app.run(debug=True)