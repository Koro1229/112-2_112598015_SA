

class Task:
    def __init__(self, id_: int, description: str, done: bool) -> None:
        self.id = id_
        self.description = description
        self.done = done

    def set_done(self, done: bool) -> None:
        self.done = done

    def is_done(self) -> bool:
        return self.done

    def generate_task_string(self) -> str:
        result = f"  [{'x' if self.is_done() else ' '}] {self.id}: {self.description}"

        return result

