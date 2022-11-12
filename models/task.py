class Task:
    def __init__(self, name, description, user, project, id=None):
        self.name = name
        self.description = description
        self.user = user
        self.project = project
        self.completed = False
        self.id = id