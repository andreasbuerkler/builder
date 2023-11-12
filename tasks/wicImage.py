import logging
from core.task import Task
from core.parameter import Parameter

class WicImage(Task):

    def __init__(self) -> None:
        Task.__init__(self, name="wicImage", after="bootBinary")

        self.fat_size = Parameter(name = "fat-size",
                                  example = "200",
                                  description = "optional, size in MByte, use default partitioning if missing")

        self.ext4_size = Parameter(name = "ext4-size",
                                   example = "500",
                                   description = "optional, no ext4 if missing")

        self.addParameterWithParent(["image"], self.fat_size)
        self.addParameterWithParent(["image"], self.ext4_size)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("fat-size = " + self.fat_size.value)
        logging.debug("ext4-size = " + self.ext4_size.value)
        logging.info("WicImage executed")


    def clean(self) -> None:
        pass

