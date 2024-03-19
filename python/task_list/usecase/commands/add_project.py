from task_list.usecase.commands.command import Command

class AddProject(Command):

    def run(self) -> None:
        result = self.task_list.add_project(self.command_rest)
        if result != "":
                self.console.print(result)
                self.console.print()