from typing import List
from task_list.entities.task_list import TaskList
from task_list.usecase.commands.command import Command

class Delete(Command):
    def run(self, task_list: TaskList) -> List[str]:
        result = task_list.delete(self.command_rest)
        return result