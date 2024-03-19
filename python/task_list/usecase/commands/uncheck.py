from task_list.usecase.commands.command import Command

class Uncheck(Command):
    def run(self, command_rest) -> None:
        result = self.backend.set_done(command_rest, False)
        if result != "":
            self.console.print(result)
            self.console.print()