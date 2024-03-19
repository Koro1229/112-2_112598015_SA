from task_list.usecase.commands.command import Command

class Error(Command):
    def run(self, command_rest) -> None:
        self.console.print(f"I don't know what the command {command_rest} is.")
        self.console.print()
