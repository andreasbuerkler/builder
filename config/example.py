from config.parameter import Parameter
from config.configTree import ConfigTree

class Example(ConfigTree):

    def __init__(self):
        ConfigTree.__init__(self)
        self.text = ""


    def _addLine(self, indentation: int, parameter: Parameter):
        self.text += "\n"
        for level in range(0, indentation):
            self.text += "    "
        self.text += parameter.name + ":"
        if parameter.example:
            self.text += " \"" + parameter.example + "\""
        if parameter.description:
            self.text += " # " + parameter.description


    def _createExampleConfig(self, parameter: Parameter, indentation: int):
        self._addLine(indentation, parameter)
        for child in parameter.children:
            indentation += 1
            self._createExampleConfig(child, indentation)
            indentation -= 1


    def getExampleConfig(self) -> str:
        self.text = ""
        self._createExampleConfig(self.getTree(), 0)
        return self.text

