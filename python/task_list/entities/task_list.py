from typing import List

from task_list.entities.project import Project
from task_list.entities.task import Task


class TaskList():
    def __init__(self):
        self.lastId: int = 0
        self.projects: List[Project] = []
    
## get_list_string
    def get_list_string(self) -> List[str]:
        taskListString = []

        for project in self.projects:
            taskListString.append(project.get_project_name())
            projectTasks = project.get_project_tasks()
            for task in projectTasks:
                taskListString.append(task.generate_task_string())
            taskListString.append("")
            
        return taskListString

## add
    def add_project(self, name: str) -> str:
        newProject = Project(name)
        self.projects.append(newProject)
        return
        # # ToDo: check if project already exists

    def add_task(self, projectName: str, description: str) -> str:
        for project in self.projects:
            if project.get_project_name() == projectName:
                project.add_task(Task(self.next_id(), description, False))
                return
        return f"Could not find a project with the name {projectName}."
    
## set_done
    def set_done(self, taskId: str, done: bool) -> str:
        # taskId = int(idString)
        for project in self.projects:
            if project.is_task_exist(taskId):
                project.set_done(taskId, done)
                return
        return f"Could not find a task with an ID of {taskId}"
    
## delete
    def delete(self, taskId: str) -> str:
        # taskId = int(idString)
        for project in self.projects:
            if project.is_task_exist(taskId):
                project.remove_task(taskId)
                return
        return f"Could not find a task with an ID of {taskId}"

## tool
    def next_id(self) -> int:
        self.lastId += 1
        return self.lastId