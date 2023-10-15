import os
import pathlib
import logging
from core.yamlParser import YamlParser
from core.exampleConfig import ExampleConfig
from core.task import Task

taskList = []

def addTask(task: Task) -> None:
    taskList.append(task)


def getPriority(module: Task) -> int:
    return module.getPriority()


def getTasksSorted() -> list[Task]:
    return sorted(taskList, key=getPriority)


def getExampleConfig() -> str:
    example = ExampleConfig()
    for task in getTasksSorted():
        example.addParameterList(task.getList())
    return example.getExampleConfig()


def executeBuild(configFilePath: str) -> None:
    if os.path.isfile(configFilePath) == False:
        logging.error("Config file does not exist")
        raise SystemExit()

    parser = None
    ending = pathlib.Path(configFilePath).suffix
    if (ending == ".yml") or (ending == ".yaml"):
        parser = YamlParser(configFilePath)

    if not parser:
        logging.error("Config file type not supported")
        raise SystemExit()

    for task in getTasksSorted():
        task.parseConfig(parser)
    for task in getTasksSorted():
        task.execute()

