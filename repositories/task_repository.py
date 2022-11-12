from db.run_sql import run_sql



def save(task):
    sql = "INSERT INTO tasks ( title, description, user_id, project_id, completed) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [task.title, task.description, task.user.id, task.project.id, task.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    
def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)