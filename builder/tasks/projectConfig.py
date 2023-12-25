import logging
from tasks.Itask import ITask
from config.parameter import Parameter
from config.configTree import ConfigTree
from core.sequence import Sequence

class ProjectConfig(ITask, ConfigTree, Sequence):

    def __init__(self) -> None:
        ConfigTree.__init__(self)
        Sequence.__init__(self, name="projectConfig", after="versionCheck")

        self.bsp = Parameter(name = "bsp",
                             parent = ["header"],
                             example = "test.bsp",
                             isOptional = True,
                             optionalCondition = ["xsa"],
                             description = "Path to BSP file")

        self.xsa= Parameter(name = "xsa",
                            parent = ["header"],
                            example = "test.xsa",
                            isOptional = True,
                            optionalCondition = ["bsp"],
                            description = "Path to XSA file")

        self.arch = Parameter(name = "arch",
                              parent = ["header"],
                              example = "zynqMP",
                              description = "zynq or zynqMP")

        self.builddir = Parameter(name = "builddir",
                                  parent = ["header"],
                                  example = "build",
                                  description = "Project name")

        self.addParameter(self.bsp)
        self.addParameter(self.xsa)
        self.addParameter(self.arch)
        self.addParameter(self.builddir)


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

