from typing import Callable
from config.parameter import Parameter
from config.configTree import ConfigTree
from parser.Iparser import IParser

class ConfigParser(ConfigTree):

    def __init__(self, parser: IParser) -> None:
        ConfigTree.__init__(self)
        self.parser = parser
        self._create()


    def _iterate(self, parentList: list[str], callback: Callable[[Parameter, ConfigTree], None], tree: ConfigTree) -> None:
        for element in self.parser.getList():
            parameter = Parameter(name = element,
                                  value = self.parser.getValue(element),
                                  parent = parentList)
            callback(parameter, tree)

            self.parser.gotoElement(element)
            parentList.append(element)
            self._iterate(parentList, callback, tree)

            parentList.pop()
        self.parser.goBack()


    def _create(self) -> None:
        self.parser.gotoRoot();
        self._iterate([], self._addParameter, self)


    def _addParameter(self, parameter: Parameter, tree: ConfigTree) -> None:
        tree.addParameter(parameter)


    def _transferValue(self, parameter: Parameter, tree: ConfigTree) -> None:
        for treeParameter in tree.getList():
            if (parameter.name == treeParameter.name) and (parameter.parent == treeParameter.parent):
                treeParameter.value = parameter.value


    def transferValues(self, config: ConfigTree) -> None:
        self.parser.gotoRoot();
        self._iterate([], self._transferValue, config)

