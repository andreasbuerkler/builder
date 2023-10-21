import logging
from core.task import Task
from core.parameter import Parameter

class CacheConfig(Task):

    def __init__(self, name: str, priority: int) -> None:
        Task.__init__(self, name, priority)

        self.download = Parameter(name = "download",
                                 example = "\"cache/dl\"",
                                 description = "",
                                 parent = "cache")
        self.sharedState = Parameter(name = "sharedState",
                                 example = "\"cache/sstate\"",
                                 description = "",
                                 parent = "cache")

        self.addParameter(Parameter(name = "cache"))
        self.addParameter(self.download)
        self.addParameter(self.sharedState)


    def execute(self) -> None:
        logging.debug("download = " + self.download.value)
        logging.debug("sharedState = " + self.sharedState.value)
        logging.info("CacheConfig executed")

