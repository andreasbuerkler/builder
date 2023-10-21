from core.task import Task
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
    taskList.append(VersionCheck("VersionCheck", 1))
    taskList.append(Repo("Repo", 2))
    taskList.append(ProjectConfig("ProjectConfig", 3))
    taskList.append(CacheConfig("CacheConfig", 4))
    taskList.append(Build("Build", 5))
    taskList.append(BootBinary("BootBinary", 6))
    taskList.append(WicImage("WicImage", 7))
    taskList.append(CopyOutput("CopyOutput", 8))
    taskList.append(CreateBsp("CreateBsp", 9))


def getTasks() -> list[Task]:
    return taskList

