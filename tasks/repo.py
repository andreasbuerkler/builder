import logging
from tasks.Itask import ITask
from config.parameter import Parameter
from config.configTree import ConfigTree
from core.sequence import Sequence

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

