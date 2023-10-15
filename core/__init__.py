import os
import pathlib
import logging
from datetime import datetime
from core.yamlParser import YamlParser
from core.exampleConfig import ExampleConfig
from core.task import Task

taskList = []
parser = None

def addTask(task: Task) -> None:
    global taskList
    taskList.append(task)


def _getPriority(module: Task) -> int:
    return module.getPriority()


def _getTasksSorted() -> list[Task]:
    global taskList
    return sorted(taskList, key=_getPriority)


def _reportTime(message: str = "") -> None:
    now = datetime.now()
    timeString = now.strftime("%d.%m.%Y %H:%M:%S")
    logging.info(message + ": " + timeString)


def getExampleConfig() -> str:
    example = ExampleConfig()
    for task in _getTasksSorted():
        example.addParameterList(task.getList())
    return example.getExampleConfig()


def configure(configFilePath: str):
    if os.path.isfile(configFilePath) == False:
        logging.error("Config file does not exist")
        raise SystemExit()

    global parser
    ending = pathlib.Path(configFilePath).suffix
    if (ending == ".yml") or (ending == ".yaml"):
        parser = YamlParser(configFilePath)
    else:
        logging.error("Config file type not supported")
        raise SystemExit()


def executeBuild() -> None:
    global parser
    if not parser:
        logging.info("Nothing to build")
        return

    _reportTime("Start Build")
    for task in _getTasksSorted():
        task.parseConfig(parser)
    for task in _getTasksSorted():
        task.execute()
    _reportTime("Build Completed")

