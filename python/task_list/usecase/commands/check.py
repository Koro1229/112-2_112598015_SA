from task_list.usecase.commands.command import Command

class Check(Command):
    def run(self, command_rest) -> None:
        result = self.backend.set_done(command_rest, True)
        if result != "":
            self.console.print(result)
            self.console.print()