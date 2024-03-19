from task_list.usecase.commands.command import Command

class AddTask(Command):

    def run(self) -> None:
        command_array = self.command_rest.split(" ", 1)
        result = self.task_list.add_task(command_array[0], command_array[1])
        if result != "":
                self.console.print(result)
                self.console.print()
