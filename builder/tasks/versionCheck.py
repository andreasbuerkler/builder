import logging
from builder.tasks.Itask import ITask
from builder.config.parameter import Parameter
from builder.config.configTree import ConfigTree
from builder.core.sequence import Sequence

class VersionCheck(ITask, ConfigTree, Sequence):

    def __init__(self) -> None:
        ConfigTree.__init__(self)
        Sequence.__init__(self, name="versionCheck")

        self.version = Parameter(name = "version",
                                 parent = ["header"],
                                 example = "2022.1",
                                 description = "Version used by project")

        self.addParameter(self.version)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("version = " + self.version.value)
        logging.info("Version executed")


    def clean(self) -> None:
        pass
