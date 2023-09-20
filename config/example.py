from config.configData import ConfigData

class Example:

    def __init__(self):
        self.tree = {}
        self.text = ""


    def addData(self, data: list[ConfigData]):
        for param in data:
            self._addChildToTree(self.tree, param)


    def _addChildToTree(self, trunk: dict, data: ConfigData):
        child = {"example": data.example,
                 "description": data.description,
                 "child": {}}

        if not data.parent:
            trunk[data.name] = child
            return

        if data.parent in trunk:
            next = trunk[data.parent]["child"]
            next[data.name] = child
        else:
            for name, branch in trunk.items():
                next = branch["child"]
                self._addChildToTree(next, data)


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
        self._createExampleConfig(self.tree, 0)
        return self.text

