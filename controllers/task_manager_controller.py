from flask import Blueprint, Flask, redirect, render_template, request

import repositories.task_repository as task_repository

tasks_blueprint = Blueprint("tasks", __name__)


@tasks_blueprint.route("/tasks")
def tasks():
    tasks = task_repository.select_all()
    return render_template("tasks/index_tasks.html", tasks = tasks)


#