from task_list.usecase.commands.command import Command

class Delete(Command):
    def run(self) -> None:
        result = self.task_list.delete(self.command_rest)
        if result != "":
            self.console.print(result)
            self.console.print()