from core.task import Task
from tasks.test import Test

taskList = []

def init() -> None:
    taskList.append(Test("Test", 6))


def getTasks() -> list[Task]:
    return taskList

