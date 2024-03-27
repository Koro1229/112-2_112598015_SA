import sys

from task_list.io.console import Console
from task_list.io.app import KataTaskList


def main():
    task_list = KataTaskList(Console(sys.stdin, sys.stdout))
    task_list.run()


if __name__ == "__main__":
    main()

