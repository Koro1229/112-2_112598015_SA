from task_list.commands.command import Command

class Show(Command):
    def run(self, command_rest) -> None:
        backend_tasks = super().get()
        for project, tasks in backend_tasks.items():
            self.console.print(project)
            for task in tasks:
                self.console.print(task.generate_task_string())
            self.console.print()