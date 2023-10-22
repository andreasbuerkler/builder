import logging
from core.task import Task
from core.parameter import Parameter

class Build(Task):

    def __init__(self, name: str, priority: int) -> None:
        Task.__init__(self, name, priority)

        self.builddir = Parameter(name = "builddir",
                                  example = "build",
                                  description = "")

        self.addParameterWithParent(["header"], self.builddir)


    def execute(self) -> None:
        logging.debug("builddir = " + self.builddir.value)
        logging.info("Build executed")

