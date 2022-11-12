from flask import Blueprint, Flask, redirect, render_template, request

import repositories.task_repository as task_repository
import repositories.user_repository as user_repository
import repositories.project_repository as project_repository

tasks_blueprint = Blueprint("tasks", __name__)

#ROUTE ALL TASKS 
@tasks_blueprint.route("/tasks")
def tasks():
    tasks = task_repository.select_all()
    return render_template("tasks/index_tasks.html", tasks = tasks)
#ROUTE EDIT TASK
@tasks_blueprint.route("/tasks/<id>/edit")
def edit_task(id):
    task = task_repository.select(id)
    users = user_repository.select_all()
    projects = project_repository.select_all()
    
    return render_template('tasks/edit.html', task = task, projects = projects, users=users)
