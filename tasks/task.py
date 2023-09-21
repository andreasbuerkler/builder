from abc import ABC, abstractmethod
from config.parser import Parser
from config.configData import ConfigData
from config.tree import Tree

class Task(ABC):

    def __init__(self, name: str, priority: int):
        self.configList = []
        self.name = name
        self.priority = priority


    def getName(self) -> str:
        return self.name


    def getPriority(self) -> int:
        return self.priority


    def getConfigList(self) -> list[ConfigData]:
        return self.configList


    def _addParameter(self, name: str, parent: str = "", example: str = "", description: str = ""):
        self.configList.append(ConfigData(parent = parent,
                                          name = name,
                                          example = example,
                                          description = description))


    def _iterateTree(self, tree: dict, parser: Parser):
        for name, branch in tree.items():
            if parser.elementIsAvailable(name):
                # TODO: store parameter in variable
                print("param: " + name + " = " + parser.getValue(name))
                parser.gotoElement(name)
                self._iterateTree(branch["child"], parser)
                parser.goBack()


    def parseConfig(self, parser: Parser):
        tree = Tree()
        tree.addData(self.configList)
        parser.gotoRoot()
        self._iterateTree(tree.getTree(), parser)


    @abstractmethod
    def execute(self):
        pass

