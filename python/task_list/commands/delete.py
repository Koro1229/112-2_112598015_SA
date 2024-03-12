from task_list.commands.command import Command

class Delete(Command):
    def run(self, command_rest) -> None:
        result = self.backend.delete(command_rest)
        if result != "":
            self.console.print(result)
            self.console.print()