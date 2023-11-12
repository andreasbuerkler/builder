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
        for afterIndex in range(index+1, len(self.elements)):
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


    def _timeout(self, counter: int) -> int:
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


    def _sortList(self) -> None:
        index = 0
        counter = len(self.elements) * len(self.elements)
        while index < len(self.elements):
            counter = self._timeout(counter)

            self._updateLists(index)
            if self._checkForwardOrder(index):
                self._moveOneBackward(index)
                index = 0
                continue

            if self._checkBackwardOrder(index):
                self._moveOneForward(index)
                index = 0
                continue

            index = index + 1

