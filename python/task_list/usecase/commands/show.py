from task_list.usecase.commands.command import Command

class Show(Command):
    def run(self, command_rest) -> None:
        backend_tasks = self.backend.get_list_string()
        for tasks in backend_tasks:
            self.console.print(tasks)
