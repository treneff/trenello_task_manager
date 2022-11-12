from db.run_sql import run_sql

from models.project import Project
import repositories.project_repository as project_repository


def save(project):
    sql = "INSERT INTO projects (name) VALUES (%s) RETURNING id"
    values = [project.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    project.id = id
    
             
def select(id):
    user = None 
    sql = "SELECT * FROM projects WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
    project = Project(result["name"], result["id"])
    return project
    
    
def delete_all():
    sql = "DELETE FROM projects"
    run_sql(sql)