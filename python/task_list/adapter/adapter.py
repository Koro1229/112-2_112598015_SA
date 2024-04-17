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

    def execute(self, commandLine: str, taskList: TaskList) -> List[str]:
        cmd = None
        commandArray = commandLine.split(" ", 1)
        command = commandArray[0]
        commandRest = command
        if len(commandArray) != 1:
            commandRest = commandArray[1]

        if command == "show":
            cmd = Show()
        elif command == "add":
            cmd, commandRest = self.create_add_command(commandRest)
        elif command == "check":
            cmd = Check()
        elif command == "uncheck":
            cmd = Uncheck()
        elif command == "help":
            cmd = Help()
        elif command == "delete":
            cmd = Delete()
        else:
            commandRest = command
            cmd = Error()

        if cmd:
            result = cmd.run(taskList, commandRest)

        return result

## tool
    def create_add_command(self, commandRest: str):
        cmd = None
        if commandRest is None:
            resultCommandRest = "add " + commandRest
            return Error(), resultCommandRest
        
        commandRestArray = commandRest.split(" ", 1)
        if len(commandRestArray) < 2:
            resultCommandRest = "add " + commandRest
            return Error(), resultCommandRest
        
        
        addObject = commandRestArray[0]

        if addObject == "project":
            cmd = AddProject()
            resultCommandRest = commandRestArray[1]
            return cmd, resultCommandRest
        elif addObject == "task":
            cmd = AddTask()
            resultCommandRest = commandRestArray[1].split(" ", 1)
            return cmd, resultCommandRest
        else:
            resultCommandRest = "add " + commandRest
            return Error(), resultCommandRest