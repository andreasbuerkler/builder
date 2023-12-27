import logging
from tasks.Itask import ITask
from config.parameter import Parameter
from config.configTree import ConfigTree
from core.sequence import Sequence

class CopyOutput(ITask, ConfigTree, Sequence):

    def __init__(self) -> None:
        ConfigTree.__init__(self)
        Sequence.__init__(self, name="copyOutput", after="wicImage")

        self.path = Parameter(name = "path",
                              parent = ["output"],
                              example = "binaries",
                              isOptional = True,
                              description = "Direcory where files are copied to")

        self.files = Parameter(name = "files",
                               parent = ["output"],
                               example = "Image.ub uboot.scr boot.bin",
                               isOptional = True,
                               requires = [self.path],
                               description = "Files separated by spaces")

        self.addParameter(self.path)
        self.addParameter(self.files)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("path = " + self.path.value)
        logging.debug("files = " + self.files.value)
        logging.info("CopyOutput executed")


    def clean(self) -> None:
        pass

