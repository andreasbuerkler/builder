import time
import logging

class Log:

    class ColorFormatter(logging.Formatter):

        def __init__(self, enableColors: bool = False) -> None:
            self.time = time.time()
            if enableColors:
                self.colorGreen = "\u001b[32m"
                self.colorRed = "\u001b[31m"
                self.colorYellow = "\u001b[33m"
                self.colorCyan = "\u001b[96m"
                self.colorReset = "\u001b[0m"
            else:
                self.colorGreen = ""
                self.colorRed = ""
                self.colorYellow = ""
                self.colorReset = ""


        def createFormatString(self, color: str, label: str, message: str) -> str:
            passedTime = f"{(time.time() - self.time):.0f}"
            return passedTime.rjust(5) + "s  " + color + label.ljust(9) + self.colorReset + message


        def format(self, record: logging.LogRecord) -> str:
            if record.levelno == logging.DEBUG:
                formatString = self.createFormatString(self.colorCyan, "DEBUG", record.getMessage())
            elif record.levelno == logging.INFO:
                formatString = self.createFormatString(self.colorGreen, "INFO", record.getMessage())
            elif record.levelno == logging.ERROR:
                formatString = self.createFormatString(self.colorRed, "ERROR", record.getMessage())
            elif record.levelno == logging.WARNING:
                formatString = self.createFormatString(self.colorYellow, "WARNING", record.getMessage())
            else:
                formatString = self.createFormatString(self.colorReset, "", record.getMessage())

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

