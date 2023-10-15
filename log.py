import logging

class Log:

    class ColorFormatter(logging.Formatter):

        def __init__(self, enableColors: bool = False) -> None:
            if enableColors:
                self.colorGreen = "\u001b[32m"
                self.colorRed = "\u001b[31m"
                self.colorYellow = "\u001b[33m"
                self.colorReset = "\u001b[0m"
            else:
                self.colorGreen = ""
                self.colorRed = ""
                self.colorYellow = ""
                self.colorReset = ""


        def format(self, record: logging.LogRecord) -> str:
            if record.levelno == logging.DEBUG:
                formatString = self.colorYellow + "DEBUG     " + self.colorReset + record.getMessage()
            elif record.levelno == logging.INFO:
                formatString = self.colorGreen + "INFO      " + self.colorReset + record.getMessage()
            elif record.levelno == logging.ERROR:
                formatString = self.colorRed + "ERROR     " + self.colorReset + record.getMessage()
            else:
                formatString = record.getMessage()

            return formatString


    def setupConsoleLogger(self, debugLevel: int) -> None:
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(Log.ColorFormatter(enableColors = True))
        streamHandler.setLevel(debugLevel)
        log = logging.getLogger()
        log.addHandler(streamHandler)
        log.setLevel(debugLevel)


    def setupFileLogger(self, fileName: str) -> None:
        fileHandler = logging.FileHandler(fileName, 'w')
        fileHandler.setFormatter(Log.ColorFormatter())
        log = logging.getLogger()
        log.addHandler(fileHandler)
        log.setLevel(logging.DEBUG)

