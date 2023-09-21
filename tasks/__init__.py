from tasks import test

Tasks = []

def getPriority(module) -> int:
    return module.getPriority()


def init():
    Tasks.append(test.Test("Test", 6))


def getTasks() -> list:
    return sorted(Tasks, key=getPriority)

