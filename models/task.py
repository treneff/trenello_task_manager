class Task:
    def __init__(self, title, description, user, project, completed=False,  id=None):
        self.title = title
        self.description = description
        self.user = user
        self.project = project
        self.completed = completed
        self.id = id
        
        
        

def get_title(task):
    return task["title"]
    
    
def get_description(task):
    return task["description"]
    
    
def get_user(task):
    return task["user"]
    
    
def get_project(task):
    return task["project"]
    
    
def get_completed(task):
    return task["completed"]

