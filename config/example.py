from config.configData import ConfigData
from config.tree import Tree

class Example:

    def __init__(self):
        self.tree = Tree()
        self.text = ""


    def addData(self, data: list[ConfigData]):
        self.tree.addData(data)


    def _addLine(self, indentation: int, name: str, example: str, description: str):
        self.text += "\n"
        for level in range(0, indentation):
            self.text += "    "
        self.text += name + ":"
        if example:
            self.text += " \"" + example + "\""
        if description:
            self.text += " # " + description


    def _createExampleConfig(self, trunk: dict, indentation: int):
        for name, branch in trunk.items():
            self._addLine(indentation, name, branch["example"], branch["description"])
            indentation += 1
            self._createExampleConfig(branch["child"], indentation)
            indentation -= 1


    def getExampleConfig(self) -> str:
        self.text = ""
        self._createExampleConfig(self.tree.getTree(), 0)
        return self.text

