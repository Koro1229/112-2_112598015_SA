from typing import List
from task_list.entities.task_list import TaskList
from task_list.usecase.commands.command import Command

class Show(Command):
    def run(self, taskList: TaskList, commandRest: str) -> List[str]:
        result = taskList.get_list_string()
        return result
