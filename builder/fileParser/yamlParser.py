from collections import deque
import logging
import yaml
from builder.fileParser.Iparser import IParser

class YamlParser(IParser):

    def __init__(self, filename: str) -> None:
        logging.debug("Loading config file: " + filename)

        with open(filename, 'r') as f:
            self.yamlData = yaml.safe_load(f)

        self.pointer = self.yamlData
        self.stack = deque()


    def gotoRoot(self) -> None:
        self.pointer = self.yamlData
        self.stack.clear()


    def goBack(self) -> None:
        if len(self.stack) > 0:
            self.pointer = self.stack.pop()


    def gotoElement(self, name: str) -> bool:
        if not self.elementIsAvailable(name):
            return False

        element = self.pointer.get(name)
        self.stack.append(self.pointer)
        self.pointer = element
        return True


    def elementIsAvailable(self, name: str) -> bool:
        try:
            element = self.pointer.get(name)
            if element is None:
                return False
            return True
        except:
            return False


    def getList(self) -> list[str]:
        tempList: list[str] = []
        if isinstance(self.pointer, dict):
            for element, unused in self.pointer.items():
                _ = unused
                tempList.append(element)
        return tempList


    def getValue(self, name: str) -> str:
        if not self.elementIsAvailable(name):
            return ""

        element = self.pointer.get(name)
        if isinstance(element, str):
            return element
        return ""
