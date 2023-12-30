import logging
from builder.tasks.Itask import ITask
from builder.config.parameter import Parameter
from builder.config.configTree import ConfigTree
from builder.core.sequence import Sequence

class CreateBsp(ITask, ConfigTree, Sequence):

    def __init__(self) -> None:
        ConfigTree.__init__(self)
        Sequence.__init__(self, name="createBsp", after="build")

        self.builddir = Parameter(name = "builddir",
                                  parent = ["header"],
                                  example = "build",
                                  description = "Project name")

        self.bsp = Parameter(name = "bsp",
                             parent = ["output"],
                             example = "test.bsp",
                             isOptional = True,
                             description = "Creat BSP with specified name")

        self.addParameter(self.builddir)
        self.addParameter(self.bsp)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("builddir = " + self.builddir.value)
        logging.debug("bsp = " + self.bsp.value)
        logging.info("CreateBsp executed")


    def clean(self) -> None:
        pass
