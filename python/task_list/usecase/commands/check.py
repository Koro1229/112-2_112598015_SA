from task_list.usecase.commands.command import Command

class Check(Command):
    def run(self) -> None:
        result = self.task_list.set_done(self.command_rest, True)
        if result != "":
            self.console.print(result)
            self.console.print()