from task_list.usecase.commands.command import Command

class Show(Command):
    def run(self) -> None:
        backend_tasks = self.task_list.get_list_string()
        for tasks in backend_tasks:
            self.console.print(tasks)
