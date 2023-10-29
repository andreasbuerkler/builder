import logging
from core.task import Task
from core.parameter import Parameter

class CopyOutput(Task):

    def __init__(self, name: str, priority: int) -> None:
        Task.__init__(self, name, priority)

        self.path = Parameter(name = "path",
                              example = "binaries",
                              description = "")

        self.files = Parameter(name = "files",
                               example = "Image.ub uboot.scr boot.bin",
                               description = "files separated by spaces")

        self.addParameterWithParent(["output"], self.path)
        self.addParameterWithParent(["output"], self.files)


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.debug("path = " + self.path.value)
        logging.debug("files = " + self.files.value)
        logging.info("CopyOutput executed")


    def clean(self) -> None:
        pass

