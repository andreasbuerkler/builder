import logging
from core.task import Task
from core.parameter import Parameter

class WicImage(Task):

    def __init__(self, name: str, priority: int) -> None:
        Task.__init__(self, name, priority)

        self.fat_size = Parameter(name = "fat-size",
                                  example = "\"200\"",
                                  description = "optional, size in MByte, use default partitioning if missing",
                                  parent = "image")
        self.ext4_size = Parameter(name = "ext4-size",
                                   example = "\"500\"",
                                   description = "optional, no ext4 if missing",
                                 parent = "image")

        self.addParameter(Parameter(name = "image"))
        self.addParameter(self.fat_size)
        self.addParameter(self.ext4_size)


    def execute(self) -> None:
        logging.debug("fat-size = " + self.fat_size.value)
        logging.debug("ext4-size = " + self.ext4_size.value)
        logging.info("WicImage executed")

