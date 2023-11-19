from abc import ABC, abstractmethod
from parser.Iparser import IParser
from core.parameter import ParameterTree
from core.configTree import ConfigTree
from core.sequence import Sequence

class Task(ABC, ConfigTree, Sequence):

    def __init__(self, name: str, before: str = "", after: str = "") -> None:
        ConfigTree.__init__(self)
        Sequence.__init__(self, name=name, before=before, after=after)


    def _iterateTree(self, branch: ParameterTree, parser: IParser) -> None:
        branch.parameter.value = parser.getValue(branch.parameter.name)
        elementIsPresent =  parser.gotoElement(branch.parameter.name)
        for child in branch.children:
            self._iterateTree(child, parser)
        if elementIsPresent:
            parser.goBack()


    def parseConfig(self, parser: IParser) -> None:
        parser.gotoRoot()
        for branch in self.getTree():
            self._iterateTree(branch, parser)


    def doPrepare(self) -> None:
        self.prepare()


    @abstractmethod
    def prepare(self) -> None:
        pass


    def doBuild(self) -> None:
        self.build()


    @abstractmethod
    def build(self) -> None:
        pass


    def doClean(self) -> None:
        self.clean()


    @abstractmethod
    def clean(self) -> None:
        pass

