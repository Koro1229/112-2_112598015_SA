from typing import List
from task_list.usecase.commands.command import Command

class Check(Command):
    def run(self) -> List[str]:
        result = self.task_list.set_done(self.command_rest, True)
        return result