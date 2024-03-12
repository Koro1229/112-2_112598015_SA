from task_list.console import Console
from task_list.commands.show import Show
from task_list.commands.add import Add
from task_list.commands.check import Check
from task_list.commands.uncheck import Uncheck
from task_list.commands.help import Help
from task_list.commands.error import Error
from task_list.commands.delete import Delete
from task_list.adapter import CommandAdapter
from task_list.backend import TaskBackend

class TaskList:
    QUIT = "quit"

    def __init__(self, console: Console) -> None:
        self.console = console
        self.backend = TaskBackend()
        self.adapter = CommandAdapter(self.console, self.backend)

    ## run until quit
    def run(self) -> None:
        while True:
            command_str = self.console.input("> ")
            if command_str == self.QUIT:
                break
            self.execute(command_str)

    ## applicaiton functions    
    def execute(self, command_line: str) -> None:
        self.adapter.execute(command_line)

