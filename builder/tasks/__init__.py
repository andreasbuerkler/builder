import logging
from datetime import datetime
from tasks.Itask import ITask
from tasks.versionCheck import VersionCheck
from tasks.repo import Repo
from tasks.projectConfig import ProjectConfig
from tasks.cacheConfig import CacheConfig
from tasks.build import Build
from tasks.bootBinary import BootBinary
from tasks.wicImage import WicImage
from tasks.copyOutput import CopyOutput
from tasks.createBsp import CreateBsp

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

