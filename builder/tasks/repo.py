import logging
from builder.tasks.Itask import ITask
from builder.config.parameter import Parameter
from builder.config.configTree import ConfigTree
from builder.core.sequence import Sequence

class Repo(ITask, ConfigTree, Sequence):

    def __init__(self) -> None:
        ConfigTree.__init__(self)
        Sequence.__init__(self, name="repo", before="build")


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.info("Repo executed")


    def clean(self) -> None:
        pass
