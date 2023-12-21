import logging
from datetime import datetime
from tasks.Itask import ITask
from core.sequence import Sequence

def _reportTime(message: str = "") -> None:
    now = datetime.now()
    timeString = now.strftime("%d.%m.%Y %H:%M:%S")
    logging.info(message + ": " + timeString)


def executeBuild(taskList: list[ITask]) -> None:
    _reportTime("Start Build")
    for task in taskList:
        task.doPrepare()
    for task in taskList:
        task.doBuild()
    for task in taskList:
        task.doClean()
    _reportTime("Build Completed")


def getTaskSequence(taskList: list[ITask]) -> list[str]:
    taskSequence: list[str] = []
    for task in taskList:
        if isinstance(task, Sequence):
            taskSequence.append(task.name)
    return taskSequence

