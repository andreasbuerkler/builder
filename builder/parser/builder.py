import pathlib
from parser.Iparser import IParser
from parser.yamlParser import YamlParser
from parser.dummyParser import DummyParser

class Builder():

    def __new__(cls, filePath: str) -> IParser:
        ending = pathlib.Path(filePath).suffix
        if (ending == ".yml") or (ending == ".yaml"):
            return YamlParser(filePath)
        else:
            return DummyParser()

