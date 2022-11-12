import pdb

from models.task import Task
import repositories.task_repository as task_repository

from models.user import User
import repositories.user_repository as user_repository

from models.project import Project
import repositories.project_repository as project_repository


# biting_repository.delete_all()
task_repository.delete_all()
project_repository.delete_all()
user_repository.delete_all()

user_1 = User('George')
project_1 = Project('Task Manager')
task_1 = Task('Get Started','A short description of how to get started', user_1, project_1)

user_repository.save(user_1)
project_repository.save(project_1)
task_repository.save(task_1)


pdb.set_trace()
