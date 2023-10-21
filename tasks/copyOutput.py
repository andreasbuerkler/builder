import logging
from core.task import Task
from core.parameter import Parameter

class CopyOutput(Task):

    def __init__(self, name: str, priority: int) -> None:
        Task.__init__(self, name, priority)

        self.path = Parameter(name = "path",
                              example = "\"binaries\"",
                              description = "",
                              parent = "output")
        self.files = Parameter(name = "files",
                                 example = "\"Image.ub uboot.scr boot.bin\"",
                                 description = "files separated by spaces",
                                 parent = "output")

        self.addParameter(Parameter(name = "output"))
        self.addParameter(self.path)
        self.addParameter(self.files)


    def execute(self) -> None:
        logging.debug("path = " + self.path.value)
        logging.debug("files = " + self.files.value)
        logging.info("CopyOutput executed")

