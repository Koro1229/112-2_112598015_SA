from task_list.io.console import Console

from task_list.usecase.commands.show import Show
from task_list.usecase.commands.add_project import AddProject
from task_list.usecase.commands.add_task import AddTask
from task_list.usecase.commands.check import Check
from task_list.usecase.commands.uncheck import Uncheck
from task_list.usecase.commands.help import Help
from task_list.usecase.commands.error import Error
from task_list.usecase.commands.delete import Delete
from task_list.usecase.commands.command import Command

class CommandFactory():
    def __init__(self, console: Console) -> None:
        self.console = console
        self.command_rest = None

    def set_command_rest(self, command_rest: str) -> None:
        self.command_rest = command_rest

    def create_show(self) -> Command:
        cmd = Show(self.console)
        return cmd
    
    def create_help(self) -> Command:
        cmd = Help(self.console)
        return cmd
    
    def create_error(self) -> Command:
        cmd = Error(self.console)
        cmd.set_command_rest(self.command_rest)
        return cmd
    
    def create_check(self) -> Command:
        cmd = Check(self.console)
        cmd.set_command_rest(self.command_rest)
        return cmd
    
    def create_uncheck(self) -> Command:
        cmd = Uncheck(self.console)
        cmd.set_command_rest(self.command_rest)
        return cmd
    
    def create_delete(self) -> Command:
        cmd = Delete(self.console)
        cmd.set_command_rest(self.command_rest)
        return cmd
    
    def create_add(self) -> Command:
        command_rest_array = self.command_rest.split(" ", 1)
        add_type = command_rest_array[0]

        if add_type == "project":
            self.set_command_rest(command_rest_array[1])
            return self.create_add_project()
        elif add_type == "task":
            self.set_command_rest(command_rest_array[1])
            return self.create_add_task()
        else:
            self.set_command_rest("add " + self.command_rest)
            return self.create_error()

    def create_add_project(self) -> Command:
        cmd = AddProject(self.console)
        cmd.set_command_rest(self.command_rest)
        return cmd

    def create_add_task(self) -> Command:
        cmd = AddTask(self.console)
        cmd.set_command_rest(self.command_rest)
        return cmd