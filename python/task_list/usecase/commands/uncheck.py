from task_list.usecase.commands.command import Command

class Uncheck(Command):
    def run(self) -> None:
        result = self.task_list.set_done(self.command_rest, False)
        if result != "":
            self.console.print(result)
            self.console.print()