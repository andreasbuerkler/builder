import logging
from builder.tasks.Itask import ITask
from builder.config.parameter import Parameter
from builder.config.configTree import ConfigTree
from builder.core.sequence import Sequence

class Build(ITask, ConfigTree, Sequence):

    def __init__(self) -> None:
        ConfigTree.__init__(self)
        Sequence.__init__(self, name="build", after="projectConfig")

        self.builddir = Parameter(name = "builddir",
                                  parent = ["header"],
                                  example = "build",
                                  description = "")

        self.addParameter(self.builddir)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("builddir = " + self.builddir.value)
        logging.info("Build executed")


    def clean(self) -> None:
        pass
