from typing import List
from task_list.usecase.commands.command import Command

class Delete(Command):
    def run(self) -> List[str]:
        result = self.task_list.delete(self.command_rest)
        return result