import logging
from core.task import Task
from core.parameter import Parameter

class VersionCheck(Task):

    def __init__(self) -> None:
        Task.__init__(self, name="versionCheck")

        self.version = Parameter(name = "version",
                                 example = "2022.1",
                                 description = "Version used by project")

        self.addParameterWithParent(["header"], self.version)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("version = " + self.version.value)
        logging.info("Version executed")


    def clean(self) -> None:
        pass

