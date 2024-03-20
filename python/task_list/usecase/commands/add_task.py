from typing import List
from task_list.usecase.commands.command import Command

class AddTask(Command):

    def run(self) -> List[str]:
        command_array = self.command_rest.split(" ", 1)
        result = self.task_list.add_task(command_array[0], command_array[1])
        return result
