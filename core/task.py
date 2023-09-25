from abc import ABC, abstractmethod
from core.parser import Parser
from core.parameter import ParameterTree
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


    def _iterateTree(self, branch: ParameterTree, parser: Parser):
        branch.parameter.value = parser.getValue(branch.parameter.name)
        elementIsPresent =  parser.gotoElement(branch.parameter.name)
        for child in branch.children:
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

