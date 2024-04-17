from typing import List
from task_list.entities.task_list import TaskList
from task_list.usecase.commands.command import Command

class Check(Command):
    def run(self, taskList: TaskList, checkedId: int) -> List[str]:
        result = taskList.set_done(checkedId, True)
        return result