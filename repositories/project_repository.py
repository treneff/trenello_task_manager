from db.run_sql import run_sql


def save(project):
    sql = "INSERT INTO projects (name) VALUES (%s) RETURNING id"
    values = [project.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    project.id = id
    
    
    
    
def delete_all():
    sql = "DELETE FROM projects"
    run_sql(sql)