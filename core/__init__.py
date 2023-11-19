import logging
from datetime import datetime
from parser.Iparser import IParser
from core.exampleConfig import ExampleConfig
from core.task import Task


def _reportTime(message: str = "") -> None:
    now = datetime.now()
    timeString = now.strftime("%d.%m.%Y %H:%M:%S")
    logging.info(message + ": " + timeString)


def getExampleConfig(taskList: list[Task]) -> str:
    example = ExampleConfig()
    for task in taskList:
        example.addParameterList(task.getList())
    return example.getExampleConfig()


def executeBuild(taskList: list[Task], parser: IParser) -> None:
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

