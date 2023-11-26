import logging
from core.task import Task
from core.parameter import Parameter

class CreateBsp(Task):

    def __init__(self) -> None:
        Task.__init__(self, name="createBsp", after="build")

        self.builddir = Parameter(name = "builddir",
                                  example = "build",
                                  description = "Project name")

        self.bsp = Parameter(name = "bsp",
                             example = "test.bsp",
                             isOptional = True,
                             description = "Creat BSP with specified name")

        self.addParameterWithParent(["header"], self.builddir)
        self.addParameterWithParent(["output"], self.bsp)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("builddir = " + self.builddir.value)
        logging.debug("bsp = " + self.bsp.value)
        logging.info("CreateBsp executed")


    def clean(self) -> None:
        pass

