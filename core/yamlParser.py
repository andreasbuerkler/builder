import logging
import yaml
from core.parser import Parser
from collections import deque

class YamlParser(Parser):

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
        list = []
        for element, unused in self.pointer.items():
            _ = unused
            list.append(element)
        return list


    def getValue(self, name: str) -> str:
        if not self.elementIsAvailable(name):
            return ""

        element = self.pointer.get(name)
        if isinstance(element, str):
            return element
        return ""

