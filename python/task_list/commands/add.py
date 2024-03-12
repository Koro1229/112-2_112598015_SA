from task_list.commands.command import Command

class Add(Command):
    def run(self, command_rest) -> None:
        sub_command_rest = command_rest.split(" ", 1)
        sub_command = sub_command_rest[0]
        if sub_command == "project":
            if len(sub_command_rest) == 1:
                self.console.print("sorry cannot find the rest command")
                return
            result = self.backend.add_project(sub_command_rest[1])
            if result != "":
                self.console.print(result)
                self.console.print()

        elif sub_command == "task":
            if len(sub_command_rest) == 1:
                self.console.print("sorry cannot find the rest command")
                return
            project_task = sub_command_rest[1].split(" ", 1)
            if len(project_task) == 1:
                self.console.print("sorry cannot find the rest command")
                return
            result = self.backend.add_task(project_task[0], project_task[1])
            if result != "":
                self.console.print(result)
                self.console.print()