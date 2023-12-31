from abc import ABC, abstractmethod

class IParser(ABC):

    @abstractmethod
    def gotoRoot(self) -> None:
        pass


    @abstractmethod
    def goBack(self) -> None:
        pass


    @abstractmethod
    def gotoElement(self, name: str) -> bool:
        return False


    @abstractmethod
    def getList(self) -> list[str]:
        return []


    @abstractmethod
    def elementIsAvailable(self, name: str) -> bool:
        return False


    @abstractmethod
    def getValue(self, name: str) -> str:
        return ""
