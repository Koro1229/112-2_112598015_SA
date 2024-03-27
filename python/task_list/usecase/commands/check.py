from typing import List
from task_list.entities.task_list import TaskList
from task_list.usecase.commands.command import Command

class Check(Command):
    def run(self, taskList: TaskList, commandRest: str) -> List[str]:
        result = taskList.set_done(int(commandRest), True)
        return result