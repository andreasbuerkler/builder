import pathlib
from builder.fileParser.Iparser import IParser
from builder.fileParser.yamlParser import YamlParser
from builder.fileParser.dummyParser import DummyParser

class Factory():

    def __new__(cls, filePath: str) -> IParser:
        ending = pathlib.Path(filePath).suffix
        if (ending == ".yml") or (ending == ".yaml"):
            return YamlParser(filePath)
        return DummyParser()
