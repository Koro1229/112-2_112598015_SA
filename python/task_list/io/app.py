from task_list.io.console import Console
from task_list.entities.task_list import TaskList
from task_list.adapter.adapter import CommandAdapter

class KataTaskList:
    QUIT = "quit"

    def __init__(self, console: Console) -> None:
        self.task_list = TaskList()
        self.console = console

    ## run until quit
    def run(self) -> None:
        while True:
            command_str = self.console.input("> ")
            if command_str == self.QUIT:
                break
            self.execute(command_str)

    ## applicaiton functions    
    def execute(self, command_line: str) -> None:
        adapter = CommandAdapter()
        result = adapter.execute(command_line, self.task_list)
        if result != None:
            for content in result:
                self.console.print(content)
