import logging
from core.task import Task
from core.parameter import Parameter

class ProjectConfig(Task):

    def __init__(self) -> None:
        Task.__init__(self, name="projectConfig", after="versionCheck")

        self.bsp = Parameter(name = "bsp",
                             example = "test.bsp",
                             isOptional = True,
                             description = "Path to BSP file")

        self.xsa= Parameter(name = "xsa",
                            example = "test.xsa",
                            isOptional = True,
                            optionalCondition = ["bsp"],
                            description = "Path to XSA file")

        self.arch = Parameter(name = "arch",
                              example = "zynqMP",
                              description = "zynq or zynqMP")

        self.builddir = Parameter(name = "builddir",
                                  example = "build",
                                  description = "Project name")

        self.addParameterWithParent(["header"], self.bsp)
        self.addParameterWithParent(["header"], self.xsa)
        self.addParameterWithParent(["header"], self.arch)
        self.addParameterWithParent(["header"], self.builddir)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("bsp = " + self.bsp.value)
        logging.debug("xsa = " + self.xsa.value)
        logging.debug("arch = " + self.arch.value)
        logging.debug("builddir = " + self.builddir.value)
        logging.info("ProjectConfig executed")


    def clean(self) -> None:
        pass

