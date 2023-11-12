import os
import pathlib
import logging
from datetime import datetime
from core.yamlParser import YamlParser
from core.exampleConfig import ExampleConfig
from core.task import Task

parser = None

def _reportTime(message: str = "") -> None:
    now = datetime.now()
    timeString = now.strftime("%d.%m.%Y %H:%M:%S")
    logging.info(message + ": " + timeString)


def getExampleConfig(taskList: list[Task]) -> str:
    example = ExampleConfig()
    for task in taskList:
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


def executeBuild(taskList: list[Task]) -> None:
    global parser
    if not parser:
        logging.info("Nothing to build")
        return

    _reportTime("Start Build")
    for task in taskList:
        task.parseConfig(parser)
    for task in taskList:
        task.doPrepare()
    for task in taskList:
        task.doBuild()
    for task in taskList:
        task.doClean()
    _reportTime("Build Completed")

