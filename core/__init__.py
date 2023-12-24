from typing import cast
from tasks.Itask import ITask
from core.sequence import Sequence, SequenceOrganizer

def getTaskSequence(taskList: list[ITask]) -> list[str]:
    taskSequence: list[str] = []
    for task in taskList:
        if isinstance(task, Sequence):
            taskSequence.append(task.name)
    return taskSequence


def sort(taskList: list[ITask]) -> list[ITask]:
    for task in taskList:
        if not isinstance(task, Sequence):
            raise Exception("element is not of type Sequence")
    organizer = SequenceOrganizer(cast(list[Sequence], taskList))
    return cast(list[ITask], organizer.getSortedList())

