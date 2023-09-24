from core.task import Task
from tasks.test import Test

TaskList = []

def getPriority(module) -> int:
    return module.getPriority()


def init():
    TaskList.append(Test("Test", 6))


def getTasks() -> list[Task]:
    return sorted(TaskList, key=getPriority)

