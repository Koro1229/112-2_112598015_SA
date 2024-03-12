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

## get
    def get(self) -> Dict[str, List[Task]]:
        return self.backend.get()

## deadline
    # def deadline(self, command_line: str) -> None:
    #     task_deadline = command_line.split(" ", 1)
    #     result = self.backend.set_deadline(task_deadline[0], task_deadline[1])
    #     if result != "":
    #         self.console.print(result)
    #         self.console.print()
