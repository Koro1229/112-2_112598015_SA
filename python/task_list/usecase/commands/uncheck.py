from typing import List
from task_list.entities.task_list import TaskList
from task_list.usecase.commands.command import Command

class Uncheck(Command):
    def run(self, task_list: TaskList, command_rest: str) -> List[str]:
        result = task_list.set_done(command_rest, False)
        return result