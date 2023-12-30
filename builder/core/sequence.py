from dataclasses import dataclass
import logging

@dataclass
class Sequence:
    name: str = ""
    before: str = ""
    after: str = ""


class SequenceOrganizer():

    def __init__(self, elements: list[Sequence]) -> None:
        self.elements = elements.copy()
        self.numberOfElements = len(elements)
        self.beforeList = []
        self.afterList = []
        self._sortList()


    def getSortedList(self) -> list[Sequence]:
        return self.elements


    def _updateLists(self, index: int) -> None:
        self.beforeList.clear()
        self.afterList.clear()
        for beforeIndex in range(0, index):
            self.beforeList.append(self.elements[beforeIndex])
        for afterIndex in range(index+1, self.numberOfElements):
            self.afterList.append(self.elements[afterIndex])


    def _checkForwardOrder(self, index: int) -> bool:
        element = self.elements[index]
        for beforeElement in self.beforeList:
            if beforeElement.name == element.before:
                return True
        return False


    def _checkBackwardOrder(self, index: int) -> bool:
        element = self.elements[index]
        for afterElement in self.afterList:
            if afterElement.name == element.after:
                return True
        return False


    def _checkForTimeout(self, counter: int) -> int:
        if counter == 0:
            logging.error("Task list dependency error")
            raise SystemExit()
        return counter - 1


    def _moveOneBackward(self, index: int) -> None:
        element = self.elements.pop(index)
        self.elements.insert(index-1, element)


    def _moveOneForward(self, index: int) -> None:
        element = self.elements.pop(index)
        self.elements.insert(index+1, element)


    def _sortForward(self) -> bool:
        updated = False
        for index in range(0, self.numberOfElements):
            self._updateLists(index)
            if self._checkForwardOrder(index):
                self._moveOneBackward(index)
                updated = True
        return updated


    def _sortBackward(self) -> bool:
        updated = False
        for index in range(0, self.numberOfElements):
            self._updateLists(index)
            if self._checkBackwardOrder(index):
                self._moveOneForward(index)
                updated = True
        return updated


    def _sortList(self) -> None:
        timeoutCounter = self.numberOfElements * self.numberOfElements
        oldCounter = timeoutCounter
        while True:
            while self._sortForward():
                timeoutCounter = self._checkForTimeout(timeoutCounter)
            while self._sortBackward():
                timeoutCounter = self._checkForTimeout(timeoutCounter)
            if oldCounter == timeoutCounter:
                break
            oldCounter = timeoutCounter
