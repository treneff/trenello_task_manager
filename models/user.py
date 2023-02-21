class User:
    def __init__(self, name, id=None):
        self.name = name 
        self.id = id
        
        
def get_name(user):
    return user["name"]