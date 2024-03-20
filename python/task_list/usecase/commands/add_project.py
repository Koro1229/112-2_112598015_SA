from typing import List
from task_list.usecase.commands.command import Command

class AddProject(Command):

    def run(self) -> List[str]:
        result = self.task_list.add_project(self.command_rest)
        return result