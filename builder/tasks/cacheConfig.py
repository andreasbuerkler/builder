import logging
from builder.tasks.Itask import ITask
from builder.config.parameter import Parameter
from builder.config.configTree import ConfigTree
from builder.core.sequence import Sequence

class CacheConfig(ITask, ConfigTree, Sequence):

    def __init__(self) -> None:
        ConfigTree.__init__(self)
        Sequence.__init__(self, name="cacheConfig", before="build", after="projectConfig")

        self.download = Parameter(name = "download",
                                  parent = ["cache"],
                                  example = "/home/user/cache/dl",
                                  isOptional = True,
                                  description = "Absolute path to download cache directory")

        self.sharedState = Parameter(name = "sharedState",
                                     parent = ["cache"],
                                     example = "/home/user/cache/sstate",
                                     isOptional = True,
                                     description = "Absolute path to shared state cache directory")

        self.addParameter(self.download)
        self.addParameter(self.sharedState)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("download = " + self.download.value)
        logging.debug("sharedState = " + self.sharedState.value)
        logging.info("CacheConfig executed")


    def clean(self) -> None:
        pass
