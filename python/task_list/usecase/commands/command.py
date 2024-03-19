from task_list.io.console import Console
from task_list.entities.task_list import TaskList

class Command:
    def __init__(self, console: Console) -> None:
        self.console = console
        self.task_list = TaskList()
        self.command_rest = None

    def set_command_rest(self, command_rest: str) -> None:
        self.command_rest = command_rest
