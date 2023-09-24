from core.parameter import Parameter
from core.configTree import ConfigTree

class Example(ConfigTree):

    def __init__(self):
        ConfigTree.__init__(self)
        self.text = ""


    def _writeNewLine(self):
        self.text += "\n"


    def _writeIndentation(self, level: int):
        for unused in range(0, level):
            _ = unused
            self.text += "    "


    def _writeLine(self, indentation: int, parameter: Parameter):
        self._writeNewLine()
        self._writeIndentation(indentation)
        self.text += parameter.name + ":"
        if parameter.example:
            self.text += " " + parameter.example
        if parameter.description:
            self.text += "   # " + parameter.description


    def _addParameterToExampleConfig(self, parameter: Parameter, indentation: int):
        self._writeLine(indentation, parameter)
        for child in parameter.children:
            indentation += 1
            self._addParameterToExampleConfig(child, indentation)
            indentation -= 1


    def getExampleConfig(self) -> str:
        self.text = ""
        for branch in self.getTree():
            self._addParameterToExampleConfig(branch, 0)
        return self.text

