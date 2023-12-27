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
                                  parent = parentList.copy())
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
        if self._parameterIsInList(parameter, tree.getList()):
            raise Exception("Duplicate parameter: " + ",".join(parameter.parent) + "," + parameter.name)
        tree.addParameter(parameter)


    def _transferValue(self, parameter: Parameter, tree: ConfigTree) -> None:
        for treeParameter in tree.getList():
            if self._compare(parameter, treeParameter):
                treeParameter.value = parameter.value


    def transferValues(self, config: ConfigTree) -> None:
        self.parser.gotoRoot();
        self._iterate([], self._transferValue, config)


    def _compare(self, first: Parameter, second: Parameter) -> bool:
        if (first.name == second.name) and (first.parent == second.parent):
            return True
        return False


    def _parameterIsInList(self, config: Parameter, parameterList: list[Parameter]) -> bool:
        for parameter in parameterList:
            if self._compare(config, parameter):
                return True
        return False


    def verify(self, configList: list[Parameter]) -> None:
        self._verifyForWrongParameter(configList)
        self._verifyForMissingParameter(configList)


    def _verifyForWrongParameter(self, configList: list[Parameter]) -> None:
        for parsedSetting in self.getList():
            setting = self._parameterIsInList(parsedSetting, configList)
            if not setting:
                raise Exception("Wrong parameter in config file: " + ",".join(parsedSetting.parent) + "," + parsedSetting.name)


    def _verifyForMissingParameter(self, configList: list[Parameter]) -> None:
        parsedList: list[Parameter] = self.getList()

        for setting in configList:

            # check for missing settings
            if not setting.isOptional and not self._parameterIsInList(setting, parsedList):
                raise Exception("Setting is missing: " + ",".join(setting.parent) + "," + setting.name)

            # setting is only optional if parameter in optionalCondition is present
            if setting.isOptional and not self._parameterIsInList(setting, parsedList):
                for condition in setting.optionalCondition:
                    if not self._parameterIsInList(condition, parsedList):
                        raise Exception("Setting is missing: " + ",".join(setting.parent) + "," + setting.name)

            # if setting exist, the parameters in requires must also be present
            if setting.isOptional and self._parameterIsInList(setting, parsedList):
                for required in setting.requires:
                    if not self._parameterIsInList(required, parsedList):
                        raise Exception("Setting is missing: " + ",".join(required.parent) + "," + required.name)

