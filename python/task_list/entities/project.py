from typing import List
from task_list.entities.task import Task

class Project:

    def __init__(self, projectName: str) -> None:
        self.projectName = projectName
        self.toDoList = List[Task]
        ##
    