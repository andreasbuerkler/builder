import os
import logging
import yaml
from config.parser import Parser
from collections import deque

class YamlParser(Parser):

    def __init__(self, filename: str):

        if os.path.exists(filename) == False:
            logging.error("Config file does not exist")
            raise SystemExit()

        logging.debug("Loading config file: " + filename)

        with open(filename, 'r') as f:
            self.yamlData = yaml.safe_load(f)

        self.pointer = self.yamlData
        self.stack = deque()


    def gotoRoot(self):
        self.pointer = self.yamlData
        self.stack.clear()


    def goBack(self):
        self.pointer = self.stack.pop()


    def gotoElement(self, name: str) -> bool:
        try:
            element = self.pointer.get(name)
            self.stack.append(self.pointer)
            self.pointer = element
            return True
        except:
            return False


    def getList(self) -> list:
        list = []
        for element, value in self.pointer.items():
            list.append(element)
        return list


    def elementIsAvailable(self, name: str) -> bool:
        try:
            element = self.pointer.get(name)
            if element is None:
                return False
            return True
        except:
            return False


    def getValue(self, name: str) -> str:
        try:
            element = self.pointer.get(name)
            if isinstance(element, str):
                return element
            return ""
        except:
            return ""

