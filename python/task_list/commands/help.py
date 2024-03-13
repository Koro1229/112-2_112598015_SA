from task_list.commands.command import Command

class Help(Command):
    def run(self, command_rest) -> None:
        self.console.print("Commands:")
        self.console.print("  show")
        self.console.print("  add project <project name>")
        self.console.print("  add task <project name> <task description>")
        self.console.print("  check <task ID>")
        self.console.print("  uncheck <task ID>")
        self.console.print("  delete <task ID>")
        self.console.print()
