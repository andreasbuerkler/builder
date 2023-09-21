from config.configData import ConfigData

class Tree:

    def __init__(self):
        self.tree = {}


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


    def getTree(self) -> dict:
        return self.tree

