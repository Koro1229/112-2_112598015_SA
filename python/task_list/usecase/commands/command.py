from typing import List

from task_list.entities.task_list import TaskList

class Command:
    def __init__(self) -> None:
        pass

    def run(self, taskList: TaskList, commandRest: str) -> List[str]:
        ## execute command function
        pass
