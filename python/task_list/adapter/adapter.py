from typing import List

from task_list.entities.task_list import TaskList
from task_list.usecase.commands.show import Show
from task_list.usecase.commands.add_project import AddProject
from task_list.usecase.commands.add_task import AddTask
from task_list.usecase.commands.check import Check
from task_list.usecase.commands.uncheck import Uncheck
from task_list.usecase.commands.help import Help
from task_list.usecase.commands.error import Error
from task_list.usecase.commands.delete import Delete
from task_list.usecase.commands.command import Command

class CommandAdapter:

    def __init__(self) -> None:
        pass

    def execute(self, command_line: str, task_list: TaskList) -> List[str]:
        cmd = None
        command_array = command_line.split(" ", 1)
        command = command_array[0]
        command_rest = command
        if len(command_array) != 1:
            command_rest = command_array[1]

        if command == "show":
            cmd = Show()
        elif command == "add":
            cmd, command_rest = self.create_add_command(command_rest)
        elif command == "check":
            cmd = Check()
        elif command == "uncheck":
            cmd = Uncheck()
        elif command == "help":
            cmd = Help()
        elif command == "delete":
            cmd = Delete()
        else:
            command_rest = command
            cmd = Error()

        if cmd:
            result = cmd.run(task_list, command_rest)

        return result

    def create_add_command(self, command_rest: str):
        cmd = None
        if command_rest is None:
            result_command_rest = "add " + command_rest
            return Error(), result_command_rest
        
        command_rest_array = command_rest.split(" ", 1)
        if len(command_rest_array) < 2:
            result_command_rest = "add " + command_rest
            return Error(), result_command_rest
        
        
        add_object = command_rest_array[0]

        if add_object == "project":
            cmd = AddProject()
            result_command_rest = command_rest_array[1]
            return cmd, result_command_rest
        elif add_object == "task":
            cmd = AddTask()
            result_command_rest = command_rest_array[1].split(" ", 1)
            return cmd, result_command_rest
        else:
            result_command_rest = "add " + command_rest
            return Error(), result_command_rest