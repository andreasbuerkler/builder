from jobs import test

Jobs = []

def getPriority(module) -> int:
    return module.getPriority()


def init():
    Jobs.append(test.Test())


def getJobs() -> list:
    return sorted(Jobs, key=getPriority)

