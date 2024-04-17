from typing import List
from task_list.entities.task_list import TaskList
from task_list.usecase.commands.command import Command

class Uncheck(Command):
    def run(self, taskList: TaskList, uncheckedId: int) -> List[str]:
        result = taskList.set_done(uncheckedId, False)
        return result