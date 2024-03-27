from typing import Optional, IO


class Console:
    def __init__(self, inputReader: IO, outputWriter: IO) -> None:
        self.inputReader = inputReader
        self.outputWriter = outputWriter

    def print(self, string: Optional[str]="", end: str="\n", flush: bool=True) -> None:
        self.outputWriter.write(string + end)
        if flush:
            self.outputWriter.flush()

    def input(self, prompt: Optional[str]="") -> str:
        self.print(prompt, end="")
        return self.inputReader.readline().strip()

    
