from abc import ABC, abstractmethod
from config.parser import Parser
from config.configData import ConfigData

class Job(ABC):

    @abstractmethod
    def getName(self) -> str:
        return ""


    @abstractmethod
    def getPriority(self) -> int:
        return 0


    @abstractmethod
    def getHelp(self) -> list[ConfigData]:
        return []


    @staticmethod
    @abstractmethod
    def parseConfig(config: Parser):
        pass


    @abstractmethod
    def execute(self):
        pass

