from flask import Blueprint, Flask, redirect, render_template, request

import repositories.task_repository as task_repository
import repositories.user_repository as user_repository
import repositories.project_repository as project_repository
from models.task import Task
from models.project import Project

projects_blueprint = Blueprint("projects", __name__)


@projects_blueprint.route("/projects")
def all_projects():
    projects = project_repository.select_all()
    return render_template("projects/index_projects.html", projects = projects)


@projects_blueprint.route("/projects/new")
def new_project():
    projects = project_repository.select_all()
    return render_template("projects/new.html", projects=projects)


@projects_blueprint.route("/projects", methods=["POST"])
def create_project():
    name = request.form["name"]
    new_project = Project(name)
    project_repository.save(new_project)
    return redirect("/projects")


@projects_blueprint.route("/projects/<id>/tasks")
def projects_tasks(id):
    tasks = task_repository.select_project_tasks(id)
    return render_template("projects/project_tasks.html",tasks = tasks)