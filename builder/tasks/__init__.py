import logging
from datetime import datetime
from builder.tasks.Itask import ITask
from builder.tasks.versionCheck import VersionCheck
from builder.tasks.repo import Repo
from builder.tasks.projectConfig import ProjectConfig
from builder.tasks.cacheConfig import CacheConfig
from builder.tasks.build import Build
from builder.tasks.bootBinary import BootBinary
from builder.tasks.wicImage import WicImage
from builder.tasks.copyOutput import CopyOutput
from builder.tasks.createBsp import CreateBsp

taskList: list[ITask] = []

def _reportTime(message: str = "") -> None:
    now = datetime.now()
    timeString = now.strftime("%d.%m.%Y %H:%M:%S")
    logging.info(message + ": " + timeString)


def init() -> None:
    taskList.append(BootBinary())
    taskList.append(Build())
    taskList.append(CacheConfig())
    taskList.append(CopyOutput())
    taskList.append(CreateBsp())
    taskList.append(ProjectConfig())
    taskList.append(Repo())
    taskList.append(VersionCheck())
    taskList.append(WicImage())


def getTasks() -> list[ITask]:
    return taskList


def setTasks(newTaskList: list[ITask]) -> None:
    global taskList
    taskList = newTaskList


def executeBuild() -> None:
    _reportTime("Start Build")
    for task in taskList:
        task.doPrepare()
    for task in taskList:
        task.doBuild()
    for task in taskList:
        task.doClean()
    _reportTime("Build Completed")
