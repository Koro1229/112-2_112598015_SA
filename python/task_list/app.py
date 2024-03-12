from task_list.console import Console
from task_list.commands.show import Show
from task_list.commands.add import Add
from task_list.commands.check import Check
from task_list.commands.uncheck import Uncheck
from task_list.commands.help import Help
from task_list.commands.error import Error
from task_list.commands.delete import Delete
# from task_list.commands.command import Command
from task_list.backend import TaskBackend

class TaskList:
    QUIT = "quit"

    def __init__(self, console: Console) -> None:
        self.console = console
        self.backend = TaskBackend()
        # self.cmd = Command(self.console, self.backend) #same console, backend

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
        if len(command_rest) == 1:
            command_rest.append("")

        if command == "show":
            cmd = Show(self.console, self.backend)
            cmd.run(command_rest[1])
        elif command == "add":
            cmd = Add(self.console, self.backend)
            cmd.run(command_rest[1])
        elif command == "check":
            cmd = Check(self.console, self.backend)
            cmd.run(command_rest[1])
        elif command == "uncheck":
            cmd = Uncheck(self.console, self.backend)
            cmd.run(command_rest[1])
        elif command == "help":
            cmd = Help(self.console, self.backend)
            cmd.run(command_rest[1])
        elif command == "delete":
            cmd = Delete(self.console, self.backend)
            cmd.run(command_rest[1])
        else:
            cmd = Error(self.console, self.backend)
            cmd.run(command_rest[0])

