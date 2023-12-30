import logging
from builder.fileParser.Iparser import IParser

class DummyParser(IParser):

    def __init__(self):
        logging.warning("Using dummy parser")


    def gotoRoot(self) -> None:
        pass


    def goBack(self) -> None:
        pass


    def gotoElement(self, name: str) -> bool:
        return True


    def elementIsAvailable(self, name: str) -> bool:
        return False


    def getList(self) -> list[str]:
        return []


    def getValue(self, name: str) -> str:
        return ""
