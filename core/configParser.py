from core.parameter import Parameter
from core.configTree import ConfigTree
from parser.Iparser import IParser

class ConfigParser(ConfigTree):

    def __init__(self, parser: IParser) -> None:
        ConfigTree.__init__(self)
        self.parser = parser
        self._create()


    def _iterateAndAdd(self, parentList: list[str] = []) -> None:
        for element in self.parser.getList():
            parameter = Parameter(name=element,
                                  value=self.parser.getValue(element))
            self.addParameterWithParent(parentList, parameter)
            
            self.parser.gotoElement(element)
            parentList.append(element)
            self._iterateAndAdd(parentList)

            parentList.pop()
        self.parser.goBack()


    def _create(self) -> None:
        self.parser.gotoRoot();
        self._iterateAndAdd()

