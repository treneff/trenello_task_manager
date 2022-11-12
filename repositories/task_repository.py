from db.run_sql import run_sql

from models.task import Task
import repositories.user_repository as user_repository
import repositories.project_repository as project_repository


#ADD A TASK TO THE DATABASE
def save(task):
    sql = "INSERT INTO tasks ( title, description, user_id, project_id, completed) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [task.title, task.description, task.user.id, task.project.id, task.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    
    
#SELECT ALL THE TASKS CURRENTLY IN THE DATABASE   
def select_all():
    tasks = []
    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row['user_id'])
        project = project_repository.select(row['project_id'])
        task = Task(row['title'], row['description'], user, project, row['completed'], row['id'] )
        tasks.append(task)
    return tasks
    
def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)