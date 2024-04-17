from typing import List
from task_list.entities.task_list import TaskList
from task_list.entities.project_name import ProjectName
from task_list.usecase.commands.command import Command

class AddProject(Command):

    def run(self, taskList: TaskList, projectName: ProjectName) -> List[str]:
        result = []
        addResult = taskList.add_project(projectName)
        if addResult:
            result.append(addResult)
        return result