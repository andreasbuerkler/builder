from tasks.task import Task

class Test(Task):

    def __init__(self, name: str, priority: int):
        Task.__init__(self, name, priority)
        self._addParameter(name = "section_1")
        self._addParameter(parent = "section_1",
                           name = "section_1_1")
        self._addParameter(parent = "section_1_1",
                           name = "param_1",
                           example = "test 1",
                           description = "test parameter 1")
        self._addParameter(parent = "section_1_1",
                           name = "param_2",
                           example = "test 2",
                           description = "test parameter 2")
        self._addParameter(parent = "section_1",
                           name = "section_1_2")
        self._addParameter(name = "section_2")
        self._addParameter(parent = "section_2",
                           name = "test_3",
                           example = "test 3",
                           description = "test parameter 2")


    def execute(self):
       pass

