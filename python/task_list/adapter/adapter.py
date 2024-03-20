from typing import List
from task_list.io.console import Console

from task_list.adapter.command_factory import CommandFactory
from task_list.usecase.commands.delete import Command

class CommandAdapter:

    def __init__(self, console: Console) -> None:
        self.console = console

    def execute(self, command_line: str) -> List[str]:
        self.cmd = None
        command_array = command_line.split(" ", 1)
        command = command_array[0]
        command_rest = command
        if len(command_array) != 1:
            command_rest = command_array[1]

        cmdFactory = CommandFactory()
        cmdFactory.set_command_rest(command_rest)

        if command == "show":
            self.cmd = cmdFactory.create_show()
        elif command == "add":
            self.cmd = cmdFactory.create_add()
        elif command == "check":
            self.cmd = cmdFactory.create_check()
        elif command == "uncheck":
            self.cmd = cmdFactory.create_uncheck()
        elif command == "help":
            self.cmd = cmdFactory.create_help()
        elif command == "delete":
            self.cmd = cmdFactory.create_delete()
        else:
            self.cmd = cmdFactory.create_error()

        if self.cmd:
            result = self.cmd.run()

        return result
