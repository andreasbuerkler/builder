from jobs.job import Job
from config.parser import Parser
from config.configData import ConfigData

class Test(Job):

    def __init__(self):
        pass


    def getName(self) -> str:
        return "Test"


    @staticmethod
    def getPriority() -> int:
        return 9


    def getHelp(self) -> list[ConfigData]:
        help = []
        help.append(ConfigData(parent = "",
                               name = "config",
                               example = "",
                               description = ""))
        help.append(ConfigData(parent = "config",
                               name = "testi",
                               example = "",
                               description = ""))
        help.append(ConfigData(parent = "testi",
                               name = "test",
                               example = "2023",
                               description = "test parameter"))
        help.append(ConfigData(parent = "config",
                               name = "hallo",
                               example = "",
                               description = ""))
        return help


    def parseConfig(self, config: Parser):
        pass


    def execute(self):
       pass

