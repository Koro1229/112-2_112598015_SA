from typing import List
from task_list.usecase.commands.command import Command

class Show(Command):
    def run(self) -> List[str]:
        result = self.task_list.get_list_string()
        return result
