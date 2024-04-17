from typing import List

from task_list.entities.task_list import TaskList
from task_list.entities.project_name import ProjectName
from task_list.usecase.commands.show import Show
from task_list.usecase.commands.add_project import AddProject
from task_list.usecase.commands.add_task import AddTask
from task_list.usecase.commands.check import Check
from task_list.usecase.commands.uncheck import Uncheck
from task_list.usecase.commands.help import Help
from task_list.usecase.commands.error import Error
from task_list.usecase.commands.delete import Delete

class CommandAdapter:

    def __init__(self) -> None:
        pass

    def execute(self, commandLine: str, taskList: TaskList) -> List[str]:
        cmd = None
        commandArray = commandLine.split(" ", 1)
        command = commandArray[0]
        result = None

        if command == "show":
            cmd = Show()
            result = cmd.run(taskList)
        elif command == "add":
            result = self.add_command(taskList, commandArray[1])
        elif command == "check":
            cmd = Check()
            checkedId = int(commandArray[1])
            result = cmd.run(taskList, checkedId)
        elif command == "uncheck":
            cmd = Uncheck()
            uncheckedId = int(commandArray[1])
            result = cmd.run(taskList, uncheckedId)
        elif command == "help":
            cmd = Help()
            result = cmd.run()
        elif command == "delete":
            cmd = Delete()
            deletedId = int(commandArray[1])
            result = cmd.run(taskList, deletedId)
        else:
            errorCommand = command
            cmd = Error()
            result = cmd.run(errorCommand)

        return result

## tool
    def add_command(self, taskList: TaskList, commandLine: str):
        cmd = None
        
        commandArray = commandLine.split(" ", 1)
        addedObject = commandArray[0]

        if addedObject == "project":
            cmd = AddProject()
            targetProject = ProjectName(commandArray[1])
            return cmd.run(taskList, targetProject)
        elif addedObject == "task":
            cmd = AddTask()
            commandRestArray = commandArray[1].split(" ", 1)
            targetProjectName = ProjectName(commandRestArray[0])
            taskDescription = commandRestArray[1]
            return cmd.run(taskList, targetProjectName, taskDescription)