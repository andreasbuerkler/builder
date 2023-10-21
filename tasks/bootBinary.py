import logging
from core.task import Task
from core.parameter import Parameter

class BootBinary(Task):

    def __init__(self, name: str, priority: int) -> None:
        Task.__init__(self, name, priority)

#        self.param_1 = Parameter(name = "param_1",
 #                                example = "test 1",
  #                               description = "test parameter 1",
  #                               parent = "section_1_1")
  #      self.param_2 = Parameter(name = "param_2",
  #                               example = "test 2",
  #                               description = "test parameter 2",
  #                               parent = "section_1_1")
  #      self.param_3 = Parameter(name = "param_3",
  #                               example = "test 3",
  #                               description = "test parameter 2",
  #                               parent = "section_2")

  #      self.addParameter(Parameter(name = "section_1"))
  #      self.addParameter(Parameter(name = "section_1_1",
  #                                  parent = "section_1"))
  #      self.addParameter(self.param_1)
  #      self.addParameter(self.param_2)
  #      self.addParameter(Parameter(name = "section_1_2",
  #                                  parent = "section_1"))
  #      self.addParameter(Parameter(name = "section_2"))
  #      self.addParameter(self.param_3)


    def execute(self) -> None:
  #      logging.debug("param_1 = " + self.param_1.value)
  #      logging.debug("param_2 = " + self.param_2.value)
  #      logging.debug("param_3 = " + self.param_3.value)
        logging.info("BootBinary executed")

