from config.exampleConfig import ExampleConfig
from config.configTree import ConfigTree
from config.configParser import ConfigParser
from config.parameter import Parameter
from tasks.Itask import ITask
from parser.Iparser import IParser

def getExampleConfig(taskList: list[ITask]) -> str:
    example = ExampleConfig()
    for task in taskList:
        if isinstance(task, ConfigTree):
            example.addParameterList(task.getList())
    return example.getExampleConfig()


def transfer(taskList: list[ITask], parser: IParser):
    parsedConfig = ConfigParser(parser)
    configList: list[Parameter] = []
    for task in taskList:
        if isinstance(task, ConfigTree):
            parsedConfig.transferValues(task)
            for config in task.getList():
                configList.append(config)
    parsedConfig.verify(configList)

