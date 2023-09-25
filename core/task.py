from abc import ABC, abstractmethod
from core.parser import Parser
from core.parameter import Parameter
from core.configTree import ConfigTree

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
        parameter.value = parser.getValue(parameter.name)
        elementIsPresent =  parser.gotoElement(parameter.name)
        for child in parameter.children:
            self._iterateTree(child, parser)
        if elementIsPresent:
            parser.goBack()


    def parseConfig(self, parser: Parser):
        parser.gotoRoot()
        for branch in self.getTree():
            self._iterateTree(branch, parser)


    @abstractmethod
    def execute(self):
        pass

