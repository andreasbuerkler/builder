from config.parameter import Parameter
from copy import deepcopy

class ConfigTree:

    def __init__(self):
        self.tree = Parameter(name = "root")


    def addParameter(self, parameter: Parameter, parent: str = ""):
        # add parameter without children, they will be added in the next iteration
        parameterCopy = deepcopy(parameter)
        parameterCopy.children.clear()
        self._addChildToTree(self.tree, parameterCopy, parent)

        parent = parameter.name
        for child in parameter.children:
            self.addParameter(child, parent)


    def _addChildToTree(self, trunk: Parameter, new: Parameter, parent: str):
        if not parent:
            trunk.children.append(new)
            return

        for child in trunk.children:
            if child.name == parent:
                child.children.append(new)
                return

        for child in trunk.children:
            self._addChildToTree(child, new, parent)


    def getTree(self) -> Parameter:
        return self.tree

