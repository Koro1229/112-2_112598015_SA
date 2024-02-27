from typing import Dict, List

from task_list.console import Console
from task_list.command import Command
from task_list.backend import TaskBackend

class TaskList:
    QUIT = "quit"

    def __init__(self, console: Console) -> None:
        self.console = console
        self.backend = TaskBackend()
        self.cmd = Command(self.console, self.backend) #same console

    ## run until quit
    def run(self) -> None:
        while True:
            command_str = self.console.input("> ")
            if command_str == self.QUIT:
                break
            self.execute(command_str)

    ## applicaiton functions    
    def execute(self, command_line: str) -> None:
        command_rest = command_line.split(" ", 1)
        command = command_rest[0]
        if command == "show":
            self.cmd.show()
        elif command == "add":
            self.cmd.add(command_rest[1])
        elif command == "check":
            self.cmd.check(command_rest[1])
        elif command == "uncheck":
            self.cmd.uncheck(command_rest[1])
        elif command == "help":
            self.cmd.help()
        else:
            self.cmd.error(command)

