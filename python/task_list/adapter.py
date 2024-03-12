from task_list.console import Console
from task_list.backend import TaskBackend

from task_list.commands.show import Show
from task_list.commands.add import Add
from task_list.commands.check import Check
from task_list.commands.uncheck import Uncheck
from task_list.commands.help import Help
from task_list.commands.error import Error
from task_list.commands.delete import Delete

class CommandAdapter:

    def __init__(self, console: Console, backend: TaskBackend) -> None:
        self.console = console
        self.backend = backend

    def execute(self, command_line: str) -> None:
        self.cmd = None
        command_rest = command_line.split(" ", 1)
        command = command_rest[0]
        if len(command_rest) == 1:
            command_rest.append("")

        if command == "show":
            self.cmd = Show(self.console, self.backend)
            self.cmd.run(command_rest[1])
        elif command == "add":
            self.cmd = Add(self.console, self.backend)
            self.cmd.run(command_rest[1])
        elif command == "check":
            self.cmd = Check(self.console, self.backend)
            self.cmd.run(command_rest[1])
        elif command == "uncheck":
            self.cmd = Uncheck(self.console, self.backend)
            self.cmd.run(command_rest[1])
        elif command == "help":
            self.cmd = Help(self.console, self.backend)
            self.cmd.run(command_rest[1])
        elif command == "delete":
            self.cmd = Delete(self.console, self.backend)
            self.cmd.run(command_rest[1])
        else:
            self.cmd = Error(self.console, self.backend)
            self.cmd.run(command_rest[0])