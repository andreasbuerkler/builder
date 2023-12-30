from builder.config.parameter import Parameter, ParameterTree
from builder.config.configTree import ConfigTree

class ExampleConfig(ConfigTree):

    def __init__(self) -> None:
        ConfigTree.__init__(self)
        self.text = ""


    def _writeNewLine(self) -> None:
        self.text += "\n"


    def _writeIndentation(self, level: int) -> None:
        for unused in range(0, level):
            _ = unused
            self.text += "    "


    def _writeLine(self, indentation: int, parameter: Parameter) -> None:
        self._writeNewLine()
        self._writeIndentation(indentation)
        self.text += parameter.name + ":"
        if parameter.example:
            self.text += " \"" + parameter.example + "\""
        if parameter.description:
            self.text += "   # " + parameter.description


    def _addParameterToExampleConfig(self, branch: ParameterTree, indentation: int) -> None:
        self._writeLine(indentation, branch.parameter)
        for child in branch.children:
            indentation += 1
            self._addParameterToExampleConfig(child, indentation)
            indentation -= 1


    def getExampleConfig(self) -> str:
        self.text = ""
        for branch in self.getTree():
            self._addParameterToExampleConfig(branch, 0)
        return self.text
