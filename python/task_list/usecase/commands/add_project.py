from typing import List
from task_list.entities.task_list import TaskList
from task_list.usecase.commands.command import Command

class AddProject(Command):

    def run(self, task_list: TaskList, command_rest: str) -> List[str]:
        result = task_list.add_project(command_rest)
        return result