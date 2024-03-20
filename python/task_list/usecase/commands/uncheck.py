from typing import List
from task_list.usecase.commands.command import Command

class Uncheck(Command):
    def run(self) -> List[str]:
        result = self.task_list.set_done(self.command_rest, False)
        return result