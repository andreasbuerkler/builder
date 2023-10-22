import logging
from core.parameter import Parameter, ParameterTree

class ConfigTree:

    def __init__(self) -> None:
        self.tree = []


    def _CheckIfParameterExists(self, trunk: list[ParameterTree], new: Parameter) -> bool:
        for branch in trunk:
            if branch.parameter.name == new.name:
                return True
        return False


    def _addChildToTree(self, branches: list[ParameterTree], new: ParameterTree) -> bool:
        for branch in branches:
            if branch.parameter.name == new.parameter.parent:
                if self._CheckIfParameterExists(branch.children, new.parameter):
                    return True
                branch.children.append(new)
                return True

            if self._addChildToTree(branch.children, new):
                return True

        return False


    def addParameterList(self, new: list[Parameter]) -> None:
        for parameter in new:
            self.addParameter(parameter)


    def addParameter(self, new: Parameter) -> None:
        if not new.parent:
            if self._CheckIfParameterExists(self.tree, new):
                return
            self.tree.append(ParameterTree(new))
            return

        if not self._addChildToTree(self.tree, ParameterTree(new)):
            logging.error("Parent not found: " + new.parent)
            raise SystemExit()


    def addParameterWithParent(self, parentList: list[str], new: Parameter):
        parent = ""
        for name in parentList:
            self.addParameter(Parameter(name = name, parent = parent))
            parent = name
        new.parent = parent
        self.addParameter(new)


    def getTree(self) -> list[ParameterTree]:
        return self.tree


    def _createList(self, parameterList: list[Parameter], branch: ParameterTree) -> None:
        parameterList.append(branch.parameter)
        for child in branch.children:
            self._createList(parameterList, child)


    def getList(self) -> list[Parameter]:
        parameterList = []
        for branch in self.tree:
            self._createList(parameterList, branch)

        return parameterList

