from db.run_sql import run_sql

from models.user import User
import repositories.user_repository as user_repository

def save(user):
    sql = "INSERT INTO users (name) VALUES (%s) RETURNING id"
    values = [user.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    user.id = id
    
        
def select(id):
    user = None 
    sql = "SELECT * FROM users WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
    user = User(result["name"], result["id"])
    return user
        
def delete_all():
    sql = "DELETE FROM users"
    run_sql(sql)