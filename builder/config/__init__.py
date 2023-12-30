from builder.config.exampleConfig import ExampleConfig
from builder.config.configTree import ConfigTree
from builder.config.configParser import ConfigParser
from builder.config.parameter import Parameter
from builder.tasks.Itask import ITask
from builder.fileParser.Iparser import IParser

def getExampleConfig(taskList: list[ITask]) -> str:
    example = ExampleConfig()
    for task in taskList:
        if isinstance(task, ConfigTree):
            example.addParameterList(task.getList())
    return example.getExampleConfig()


def transfer(taskList: list[ITask], configFileParser: IParser):
    parsedConfig = ConfigParser(configFileParser)
    configList: list[Parameter] = []
    for task in taskList:
        if isinstance(task, ConfigTree):
            parsedConfig.transferValues(task)
            for config in task.getList():
                configList.append(config)
    parsedConfig.verify(configList)
