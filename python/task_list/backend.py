from typing import Dict, List

from task_list.task import Task

class TaskBackend:
    def __init__(self):
        self.last_id: int = 0
        self.tasks: Dict[str, List[Task]] = dict()

## get
    def get(self) -> Dict[str, List[Task]]:
        return self.tasks

## add
    def add_project(self, name: str) -> str:
        project_name = self.tasks.get(name)
        if project_name is None:
            self.tasks[name] = []
            return ""
        else:
            return f"{project_name} already exists."
        

    def add_task(self, project: str, description: str) -> str:
        project_tasks = self.tasks.get(project)
        if project_tasks is None:
            return f"Could not find a project with the name {project}."
        else:
            project_tasks.append(Task(self.next_id(), description, False))
            return ""

    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id
    
## set_done
    def set_done(self, id_string: str, done: bool) -> str:
        id_ = int(id_string)
        for project, tasks in self.tasks.items():
            for task in tasks:
                if task.id == id_:
                    task.set_done(done)
                    return ""
        return f"Could not find a task with an ID of {id_}"
    
## delete
    def delete(self, id_string: str) -> str:
        id_ = int(id_string)
        for project, tasks in self.tasks.items():
            for task in tasks:
                if task.id == id_:
                    tasks.remove(task)
                    return ""
        return f"Could not find a task with an ID of {id_}"