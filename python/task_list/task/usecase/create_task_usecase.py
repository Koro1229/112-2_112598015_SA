from task_list.task.entity.task import Task

class CreateTaskUsecase:
    def execute(id: int, description: str, done: bool) -> Task:
        new_task = Task()
        new_task.set_id(id)
        new_task.set_description(description)
        new_task.set_done(done)
        return new_task
