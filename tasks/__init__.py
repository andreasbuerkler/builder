from typing import cast
from tasks.Itask import ITask
from core.sequence import SequenceOrganizer
from tasks.versionCheck import VersionCheck
from tasks.repo import Repo
from tasks.projectConfig import ProjectConfig
from tasks.cacheConfig import CacheConfig
from tasks.build import Build
from tasks.bootBinary import BootBinary
from tasks.wicImage import WicImage
from tasks.copyOutput import CopyOutput
from tasks.createBsp import CreateBsp

taskList = []

def init() -> None:
    taskList.append(VersionCheck())
    taskList.append(Repo())
    taskList.append(ProjectConfig())
    taskList.append(CacheConfig())
    taskList.append(Build())
    taskList.append(BootBinary())
    taskList.append(WicImage())
    taskList.append(CopyOutput())
    taskList.append(CreateBsp())


def getTasks() -> list[ITask]:
    organizer = SequenceOrganizer(taskList)
    return cast(list[ITask], organizer.getSortedList())

