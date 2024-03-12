from task_list.console import Console
from task_list.backend import TaskBackend

class Command:
    def __init__(self, console: Console, backend: TaskBackend) -> None:
        self.console = console
        self.backend = backend

    def run(self, command_rest: str) -> None:
        pass
