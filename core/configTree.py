import logging
from core.parameter import Parameter
from copy import deepcopy

class ConfigTree:

    def __init__(self):
        self.tree = []


    def _createCopyWithoutChildren(self, parameter: Parameter) -> Parameter:
        copy = deepcopy(parameter)
        copy.children.clear()
        return copy


    def _addChildToTree(self, branch: Parameter, new: Parameter, parent: str) -> bool:
        if branch.name == parent:
            branch.children.append(self._createCopyWithoutChildren(new))
            return True

        for child in branch.children:
            if self._addChildToTree(child, new, parent):
                return True

        return False


    def _addParameterRecursive(self, new: Parameter, parent: str = ""):
        parameterAdded = False
        for branch in self.tree:
            parameterAdded = parameterAdded or self._addChildToTree(branch, new, parent)

        if not parameterAdded:
            logging.error("Parent not found: " + parent)
            raise SystemExit()

        parent = new.name
        for child in new.children:
            self._addParameterRecursive(child, parent)


    def addParameterList(self, new: list[Parameter], parent: str = ""):
        for parameter in new:
            self.addParameter(parameter, parent)


    def addParameter(self, new: Parameter, parent: str = ""):
        if not parent:
            self.tree.append(self._createCopyWithoutChildren(new))
            self.addParameterList(new.children, new.name)
            return

        self._addParameterRecursive(new, parent)


    def getTree(self) -> list[Parameter]:
        return self.tree

