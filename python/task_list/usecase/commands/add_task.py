from typing import List
from task_list.entities.task_list import TaskList
from task_list.entities.project_name import ProjectName
from task_list.usecase.commands.command import Command

class AddTask(Command):

    def run(self, taskList: TaskList, targetProjectName: ProjectName, taskDescription: str) -> List[str]:
        result = []
        addResult = taskList.add_task(targetProjectName, taskDescription)
        if addResult:
            result.append(addResult)
        return result
