import logging
from core.task import Task
from core.parameter import Parameter

class Repo(Task):

    def __init__(self, name: str, priority: int) -> None:
        Task.__init__(self, name, priority)


    def execute(self) -> None:
        logging.info("Repo executed")

