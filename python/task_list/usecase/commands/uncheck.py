from typing import List
from task_list.entities.task_list import TaskList
from task_list.usecase.commands.command import Command

class Uncheck(Command):
    def run(self, taskList: TaskList, commandRest: str) -> List[str]:
        result = taskList.set_done(commandRest, False)
        return result