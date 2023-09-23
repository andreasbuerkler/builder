from abc import ABC, abstractmethod
from config.parser import Parser
from config.parameter import Parameter
from config.configTree import ConfigTree

class Task(ABC, ConfigTree):

    def __init__(self, name: str, priority: int):
        ConfigTree.__init__(self)
        self.name = name
        self.priority = priority


    def getName(self) -> str:
        return self.name


    def getPriority(self) -> int:
        return self.priority


    def _iterateTree(self, parameter: Parameter, parser: Parser):
        print("param: " + parameter.name + " = " + parser.getValue(parameter.name))
        elementIsPresent =  parser.gotoElement(parameter.name)
        for child in parameter.children:
            self._iterateTree(child, parser)
        if elementIsPresent:
            parser.goBack()


    def parseConfig(self, parser: Parser):
        parser.gotoRoot()
        self._iterateTree(self.getTree(), parser)


    @abstractmethod
    def execute(self):
        pass

