from task_list.io.console import Console
from task_list.adapter.adapter import CommandAdapter

class TaskList:
    QUIT = "quit"

    def __init__(self, console: Console) -> None:
        self.console = console
        self.adapter = CommandAdapter(self.console)

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

