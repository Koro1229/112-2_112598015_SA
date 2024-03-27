from typing import Dict, List

from task_list.entities.task import Task


class TaskList():
    def __init__(self):
        self.lastId: int = 0
        self.tasks: Dict[str, List[Task]] = dict()

## get
    def get(self) -> Dict[str, List[Task]]:
        return self.tasks
    
## get_list
    def get_list_string(self) -> List[str]:
        taskListString = []
        for project, tasks in self.tasks.items():
            taskListString.append(project)
            for task in tasks:
                taskListString.append(task.generate_task_string())
            taskListString.append("")
        return taskListString

## add
    def add_project(self, name: str) -> str:
        projectName = self.tasks.get(name)
        if projectName is None:
            self.tasks[name] = []
            return ""
        else:
            return f"{projectName} already exists."
        

    def add_task(self, project: str, description: str) -> str:
        projectTasks = self.tasks.get(project)
        if projectTasks is None:
            return f"Could not find a project with the name {project}."
        else:
            projectTasks.append(Task(self.next_id(), description, False))
            return ""

    def next_id(self) -> int:
        self.lastId += 1
        return self.lastId
    
## set_done
    def set_done(self, idString: str, done: bool) -> str:
        id_ = int(idString)
        for project, tasks in self.tasks.items():
            for task in tasks:
                if task.id == id_:
                    task.set_done(done)
                    return ""
        return f"Could not find a task with an ID of {id_}"
    
## delete
    def delete(self, idString: str) -> str:
        id_ = int(idString)
        for project, tasks in self.tasks.items():
            for task in tasks:
                if task.id == id_:
                    tasks.remove(task)
                    return ""
        return f"Could not find a task with an ID of {id_}"