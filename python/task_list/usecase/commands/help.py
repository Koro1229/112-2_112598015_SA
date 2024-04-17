from typing import List
from task_list.entities.task_list import TaskList
from task_list.usecase.commands.command import Command

class Help(Command):
    def run(self) -> List[str]:
        result = []
        result.append("Commands:")
        result.append("  show")
        result.append("  add project <project name>")
        result.append("  add task <project name> <task description>")
        result.append("  check <task ID>")
        result.append("  uncheck <task ID>")
        result.append("  delete <task ID>")
        result.append("")
        return result

