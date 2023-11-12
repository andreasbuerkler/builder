import logging
from core.task import Task
from core.parameter import Parameter

class Repo(Task):

    def __init__(self) -> None:
        Task.__init__(self, name="repo", before="build")


    def prepare(self) -> None:
        pass


    def build(self) -> None:
        logging.info("Repo executed")


    def clean(self) -> None:
        pass

