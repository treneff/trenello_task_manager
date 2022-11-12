from db.run_sql import run_sql


def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING id"
    values = [user.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    
    
    
def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)