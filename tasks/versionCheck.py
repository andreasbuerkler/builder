import logging
from core.task import Task
from core.parameter import Parameter

class VersionCheck(Task):

    def __init__(self, name: str, priority: int) -> None:
        Task.__init__(self, name, priority)

        self.version = Parameter(name = "version",
                                 example = "2022.1",
                                 description = "")

        self.addParameterWithParent(["header"], self.version)


    def execute(self) -> None:
        logging.debug("version = " + self.version.value)
        logging.info("Version executed")

