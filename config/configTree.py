from config.parameter import Parameter, ParameterTree

class ConfigTree:

    def __init__(self) -> None:
        self.tree: list[ParameterTree] = []


    def _CheckIfParameterExists(self, trunk: list[ParameterTree], new: Parameter) -> bool:
        for branch in trunk:
            if branch.parameter.name == new.name:
                return True
        return False


    def addParameter(self, new: Parameter) -> None:
        tree: list[ParameterTree] = self.tree

        # find parent / add parent if not existing
        parentList: list[str] = []
        for parent in new.parent:

            if not tree:
                newBranch = ParameterTree(parameter = Parameter(name = parent, parent = parentList.copy()))
                tree.append(newBranch)
                tree = newBranch.children
                parentList.append(parent)
                break

            for branch in tree:
                if branch.parameter.name == parent:
                    tree = branch.children
                    break
                if branch == tree[-1]:
                    newBranch = ParameterTree(parameter = Parameter(name = parent, parent = parentList.copy()))
                    tree.append(newBranch)
                    tree = newBranch.children
                    break

            parentList.append(parent)

        if self._CheckIfParameterExists(tree, new):
            return
        tree.append(ParameterTree(parameter = new))


    def addParameterList(self, new: list[Parameter]) -> None:
        for parameter in new:
            self.addParameter(parameter)


    def getTree(self) -> list[ParameterTree]:
        return self.tree


    def _createList(self, parameterList: list[Parameter], branch: ParameterTree) -> None:
        parameterList.append(branch.parameter)
        for child in branch.children:
            self._createList(parameterList, child)


    def getList(self) -> list[Parameter]:
        parameterList: list[Parameter] = []
        for branch in self.tree:
            self._createList(parameterList, branch)

        return parameterList

