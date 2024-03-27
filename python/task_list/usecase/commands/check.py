from typing import List
from task_list.entities.task_list import TaskList
from task_list.usecase.commands.command import Command

class Check(Command):
    def run(self, task_list: TaskList) -> List[str]:
        result = task_list.set_done(self.command_rest, True)
        return result