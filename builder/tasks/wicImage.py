import logging
from tasks.Itask import ITask
from config.parameter import Parameter
from config.configTree import ConfigTree
from core.sequence import Sequence

class WicImage(ITask, ConfigTree, Sequence):

    def __init__(self) -> None:
        ConfigTree.__init__(self)
        Sequence.__init__(self, name="wicImage", after="bootBinary")

        self.fat_size = Parameter(name = "fat-size",
                                  parent = ["image"],
                                  example = "200",
                                  isOptional = True,
                                  description = "size in MByte, use default partitioning if missing")

        self.ext4_size = Parameter(name = "ext4-size",
                                   parent = ["image"],
                                   example = "500",
                                   isOptional = True,
                                   description = "no ext4 if missing")

        self.addParameter(self.fat_size)
        self.addParameter(self.ext4_size)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("fat-size = " + self.fat_size.value)
        logging.debug("ext4-size = " + self.ext4_size.value)
        logging.info("WicImage executed")


    def clean(self) -> None:
        pass

