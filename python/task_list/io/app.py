from task_list.io.console import Console
from task_list.entities.task_list import TaskList
from task_list.adapter.adapter import CommandAdapter

class KataTaskList:
    QUIT = "quit"

    def __init__(self, console: Console) -> None:
        self.taskList = TaskList()
        self.console = console

    ## run until quit
    def run(self) -> None:
        while True:
            commandStr = self.console.input("> ")
            if commandStr == self.QUIT:
                break
            self.execute(commandStr)

    ## execute command   
    def execute(self, commandLine: str) -> None:
        adapter = CommandAdapter()
        result = adapter.execute(commandLine, self.taskList)
        if result != None:
            for content in result:
                self.console.print(content)
