from task_list.io.console import Console
from task_list.entities.task_list import TaskList

class Command:
    def __init__(self, console: Console) -> None:
        self.console = console
        self.backend = TaskList()
