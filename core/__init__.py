from core.yamlParser import YamlParser
from core.exampleConfig import ExampleConfig
from core.task import Task

taskList = []

def addTask(task: Task):
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


def executeBuild(configFilePath: str):
    parser = YamlParser(configFilePath)
    for task in getTasksSorted():
        task.parseConfig(parser)
    for task in getTasksSorted():
        task.execute()

