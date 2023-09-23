from tasks.task import Task
from config.parameter import Parameter

class Test(Task):

    def __init__(self, name: str, priority: int):
        Task.__init__(self, name, priority)
        self.addParameter(Parameter(name = "section_1"))
        self.addParameter(Parameter(name = "section_1_1"),
                          parent = "section_1")
        self.addParameter(Parameter(name = "param_1",
                                    example = "test 1",
                                    description = "test parameter 1"),
                          parent = "section_1_1")
        self.addParameter(Parameter(name = "param_2",
                                    example = "test 2",
                                    description = "test parameter 2"),
                          parent = "section_1_1")
        self.addParameter(Parameter(name = "section_1_2"),
                          parent = "section_1")
        self.addParameter(Parameter(name = "section_2"))
        self.addParameter(Parameter(name = "test_3",
                                    example = "test 3",
                                    description = "test parameter 2"),
                          parent = "section_2")


    def execute(self):
        print("Test executed")

