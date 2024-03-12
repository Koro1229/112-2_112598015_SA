from task_list.commands.command import Command

class Add(Command):
    def run(self, command_rest) -> None:
        sub_command_rest = command_rest.split(" ", 1)
        sub_command = sub_command_rest[0]
        if sub_command == "project":
            if self.is_command_rest(sub_command_rest):
                return

            result = self.backend.add_project(sub_command_rest[1])
            if result != "":
                self.console.print(result)
                self.console.print()

        elif sub_command == "task":
            if self.is_command_rest(sub_command_rest):
                return
            
            project_task = sub_command_rest[1].split(" ", 1)
            if self.is_command_rest(project_task):
                return
            
            result = self.backend.add_task(project_task[0], project_task[1])
            if result != "":
                self.console.print(result)
                self.console.print()


    def is_command_rest(self, command_rest) -> bool:
        if len(command_rest) == 1:
            self.console.print("sorry cannot find the rest command")
            return True
        return False
