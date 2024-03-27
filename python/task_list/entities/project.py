from typing import List
from task_list.entities.task import Task

class Project:

    def __init__(self, projectName: str) -> None:
        self.projectName: str = projectName
        self.toDoList: List[Task] = []
        ##
    def get_project_name(self) -> str:
        return self.projectName
    
    def get_project_tasks(self) -> List[Task]:
        return self.toDoList

    def add_task(self, newTask: Task) -> None:
        self.toDoList.append(newTask)

    def is_task_exist(self, taskId: int) -> bool:
        for task in self.toDoList:
            if task.get_id() == taskId:
                return True
        return False
    
    def set_done(self, taskId: int, done: bool) -> None:
        for task in self.toDoList:
            if task.get_id() == taskId:
                task.set_done(done)
    
    def remove_task(self, taskId: int) -> None:
        for task in self.toDoList:
            if task.get_id() == taskId:
                self.toDoList.remove(task)
