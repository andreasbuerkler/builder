import logging
from core.task import Task
from core.parameter import Parameter

class CacheConfig(Task):

    def __init__(self) -> None:
        Task.__init__(self, name="cacheConfig", before="build", after="projectConfig")

        self.download = Parameter(name = "download",
                                 example = "cache/dl",
                                 description = "")

        self.sharedState = Parameter(name = "sharedState",
                                 example = "cache/sstate",
                                 description = "")

        self.addParameterWithParent(["cache"], self.download)
        self.addParameterWithParent(["cache"], self.sharedState)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("download = " + self.download.value)
        logging.debug("sharedState = " + self.sharedState.value)
        logging.info("CacheConfig executed")


    def clean(self) -> None:
        pass

