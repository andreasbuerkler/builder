class Priority():

    def __init__(self, name: str, before: str, after: str) -> None:
        self.name = name
        self.before = before
        self.after = after


    def getName(self) -> str:
        return self.name


    def getBefore(self) -> str:
        return self.before


    def getAfter(self) -> str:
        return self.after


    @staticmethod
    def _returnLower(first: "Priority", second: "Priority") -> "Priority":
        if (first.before == second.getName()) or (second.after == first.getName()):
            return second
        return first


    @staticmethod
    def _popHighest(unsortedList: list["Priority"]) -> "Priority":
        candidates = unsortedList.copy()
        while (len(candidates) > 1):
            candidates.remove(Priority._returnLower(candidates[0], candidates[1]))
        unsortedList.remove(candidates[0])
        return candidates[0]


    @staticmethod
    def sortList(taskList: list["Priority"]) -> list["Priority"]:
        unsortedList = taskList.copy()
        sortedList = []
        while (len(unsortedList) > 0):
            sortedList.append(Priority._popHighest(unsortedList))
        return sortedList

