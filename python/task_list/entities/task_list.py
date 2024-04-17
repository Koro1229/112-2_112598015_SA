from typing import List

from task_list.entities.project import Project
from task_list.entities.project_name import ProjectName
from task_list.entities.task import Task


class TaskList():
    def __init__(self):
        self.lastId: int = 0
        self.projects: List[Project] = []
    
## get_list_string
    def get_list_string(self) -> List[str]:
        taskListString = []

        for project in self.projects:
            taskListString.append(project.get_project_name().get_string())
            projectTasks = project.get_project_tasks()
            for task in projectTasks:
                taskListString.append(task.generate_task_string())
            taskListString.append("")
            
        return taskListString

## add
    def add_project(self, projectName: ProjectName) -> str:
        newProject = Project(projectName)
        self.projects.append(newProject)
        return

    def add_task(self, projectName: ProjectName, description: str) -> str:
        for project in self.projects:
            if project.get_project_name().get_string() == projectName.get_string():
                project.add_task(Task(self.next_id(), description))
                return
        return f"Could not find a project with the name {projectName}."
    
## set_done
    def set_done(self, taskId: int, done: bool) -> str:
        for project in self.projects:
            if project.is_task_exist(taskId):
                project.set_done(taskId, done)
                return
        return f"Could not find a task with an ID of {taskId}"
    
## delete
    def delete(self, taskId: int) -> str:
        for project in self.projects:
            if project.is_task_exist(taskId):
                project.remove_task(taskId)
                return
        return f"Could not find a task with an ID of {taskId}"

## tool
    def next_id(self) -> int:
        self.lastId += 1
        return self.lastId