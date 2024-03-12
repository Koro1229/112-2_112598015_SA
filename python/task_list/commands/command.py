from typing import Dict, List

from task_list.console import Console
from task_list.task import Task
from task_list.backend import TaskBackend

class Command:
    def __init__(self, console: Console, backend: TaskBackend) -> None:
        self.console = console
        self.backend = backend

    def run(self, command_rest: str) -> None:
        pass

##show
        
    # def show(self) -> None:
    #     backend_tasks = self.get()
    #     for project, tasks in backend_tasks.items():
    #         self.console.print(project)
    #         for task in tasks:
    #             # self.console.print(f"  [{'x' if task.is_done() else ' '}] {task.id}: {task.description}")
    #             self.console.print(task.generate_task_string())
    #         self.console.print()

## add
            
    # def add(self, command_line: str = None) -> None:
    #     sub_command_rest = command_line.split(" ", 1)
    #     sub_command = sub_command_rest[0]
    #     if sub_command == "project":
    #         result = self.backend.add_project(sub_command_rest[1])
    #         if result != "":
    #             self.console.print(result)
    #             self.console.print()

    #     elif sub_command == "task":
    #         project_task = sub_command_rest[1].split(" ", 1)
    #         result = self.backend.add_task(project_task[0], project_task[1])
    #         if result != "":
    #             self.console.print(result)
    #             self.console.print()


##un/check
    
    # def check(self, id_string: str) -> None:
    #     result = self.backend.set_done(id_string, True)
    #     if result != "":
    #         self.console.print(result)
    #         self.console.print()
            
    # def uncheck(self, id_string: str) -> None:
    #     result = self.backend.set_done(id_string, False)
    #     if result != "":
    #         self.console.print(result)
    #         self.console.print()

## help
        
    # def help(self) -> None:
    #     self.console.print("Commands:")
    #     self.console.print("  show")
    #     self.console.print("  add project <project name>")
    #     self.console.print("  add task <project name> <task description>")
    #     self.console.print("  check <task ID>")
    #     self.console.print("  uncheck <task ID>")
    #     self.console.print("  delete <task ID>")
    #     self.console.print()

## error
        
    # def error(self, command: str) -> None:
    #     self.console.print(f"I don't know what the command {command} is.")
    #     self.console.print()

## get
    def get(self) -> Dict[str, List[Task]]:
        return self.backend.get()

## delete
    def delete(self, id_string: str) -> None:
        result = self.backend.delete(id_string)
        if result != "":
            self.console.print(result)
            self.console.print()

## deadline
    # def deadline(self, command_line: str) -> None:
    #     task_deadline = command_line.split(" ", 1)
    #     result = self.backend.set_deadline(task_deadline[0], task_deadline[1])
    #     if result != "":
    #         self.console.print(result)
    #         self.console.print()
