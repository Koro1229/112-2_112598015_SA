from typing import Dict, List

from task_list.console import Console
from task_list.task import Task
from task_list.command import Command

class TaskList:
    QUIT = "quit"

    def __init__(self, console: Console) -> None:
        self.console = console
        self.cmd = Command(console) #same console

    def run(self) -> None:
        while True:
            command_str = self.console.input("> ")
            if command_str == self.QUIT:
                break
            self.execute(command_str)

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

