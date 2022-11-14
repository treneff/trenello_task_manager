from flask import Blueprint, Flask, redirect, render_template, request

import repositories.task_repository as task_repository
import repositories.user_repository as user_repository
import repositories.project_repository as project_repository
from models.task import Task

tasks_blueprint = Blueprint("tasks", __name__)

#ROUTE ALL TASKS 
@tasks_blueprint.route("/tasks")
def tasks():
    tasks = task_repository.select_all()
    return render_template("tasks/index_tasks.html", tasks = tasks)

#ROUTE NEW TASK --- NEEDS REFORMATTING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
@tasks_blueprint.route("/tasks/new")
def new_task():
    users = user_repository.select_all()
    projects = project_repository.select_all()
    return render_template("tasks/new.html", users=users, projects=projects)

#ROUTE CREATE TASK
@tasks_blueprint.route("/tasks", methods=["POST"])
def create_task():
    user_id = request.form["user_id"]
    project_id = request.form["project_id"]
    title = request.form["title"]
    description = request.form["description"]
    user = user_repository.select(user_id)
    project = project_repository.select(project_id)
    new_task = Task(title, description, user, project)
    task_repository.save(new_task)
    return redirect("/tasks")

#ROUTE SHOW TASK
@tasks_blueprint.route("/tasks/<id>", methods=['GET'])
def show_task(id):
    task = task_repository.select(id)
    return render_template('tasks/show.html', task = task)

#ROUTE EDIT TASK
@tasks_blueprint.route("/tasks/<id>/edit")
def edit_task(id):
    task = task_repository.select(id)
    users = user_repository.select_all()
    projects = project_repository.select_all()
    
    return render_template('tasks/edit.html', task = task, projects = projects, users=users)

#ROUTE UPDATE TASK
@tasks_blueprint.route("/tasks/<id>", methods=['POST'])
def update_task(id):
    title = request.form['title']
    description = request.form['description']
    user = user_repository.select(request.form['user_id'])
    project  = project_repository.select(request.form['project_id'])
    task = Task(title, description, user, project, False, id )
    task_repository.update(task)
    return redirect('/tasks')

#ROUTE DELETE A TASK
@tasks_blueprint.route("/tasks/<id>/delete", methods=['POST'])
def delete_task(id):
    task_repository.delete(id)
    return redirect('/tasks')

