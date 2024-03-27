from typing import List
from task_list.entities.task_list import TaskList
from task_list.usecase.commands.command import Command

class AddTask(Command):

    def run(self, task_list: TaskList) -> List[str]:
        command_array = self.command_rest.split(" ", 1)
        result = task_list.add_task(command_array[0], command_array[1])
        return result
