from abc import ABC, abstractmethod

class ITask(ABC):

    def doPrepare(self) -> None:
        self.prepare()


    @abstractmethod
    def prepare(self) -> None:
        pass


    def doBuild(self) -> None:
        self.build()


    @abstractmethod
    def build(self) -> None:
        pass


    def doClean(self) -> None:
        self.clean()


    @abstractmethod
    def clean(self) -> None:
        pass

