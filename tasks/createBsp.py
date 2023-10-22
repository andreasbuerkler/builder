import logging
from core.task import Task
from core.parameter import Parameter

class CreateBsp(Task):

    def __init__(self, name: str, priority: int) -> None:
        Task.__init__(self, name, priority)

        self.builddir = Parameter(name = "builddir",
                                  example = "build",
                                  description = "")

        self.bsp = Parameter(name = "bsp",
                             example = "test.bsp",
                             description = "optional, create bsp")

        self.addParameterWithParent(["header"], self.builddir)
        self.addParameterWithParent(["output"], self.bsp)


    def execute(self) -> None:
        logging.debug("builddir = " + self.builddir.value)
        logging.debug("bsp = " + self.bsp.value)
        logging.info("CreateBsp executed")

