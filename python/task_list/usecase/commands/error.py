from typing import List
from task_list.entities.task_list import TaskList
from task_list.usecase.commands.command import Command

class Error(Command):
    def run(self, task_list: TaskList, command_rest: str) -> List[str]:
        result =[]
        result.append(f"I don't know what the command {command_rest} is.")
        result.append("")
        return result
