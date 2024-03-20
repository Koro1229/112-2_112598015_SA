from typing import List
from task_list.usecase.commands.command import Command

class Error(Command):
    def run(self) -> List[str]:
        result =[]
        result.append(f"I don't know what the command {self.command_rest} is.")
        result.append("")
        return result
