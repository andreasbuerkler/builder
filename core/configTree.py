import logging
from core.parameter import Parameter
from copy import deepcopy

class ConfigTree:

    def __init__(self):
        self.tree = []


    def _createCopyWithoutChildren(self, parameter: Parameter) -> Parameter:
        # No copy is needed when parameter has no children
        if not parameter.children:
            return parameter

        # TODO: avoid copy
        copy = deepcopy(parameter)
        copy.children.clear()
        return copy


    def _addChildToTree(self, branches: list[Parameter], new: Parameter, parent: str) -> bool:
        for branch in branches:
            if branch.name == parent:
                branch.children.append(self._createCopyWithoutChildren(new))
                return True

            if self._addChildToTree(branch.children, new, parent):
                return True

        return False


    def _addParameterRecursive(self, new: Parameter, parent: str = ""):
        if not self._addChildToTree(self.tree, new, parent):
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

