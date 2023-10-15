import logging
import colorlog

class Log:

    def getCustomLogLevel(self, name: str) -> int:
        # use a level between 10 (INFO) and 20 (DEBUG)
        if name == "DEBUG_DIFF":
            return 11
        elif name == "DEBUG_SHELL":
            return 12
        # use a level between 40 (ERROR) and 50 (CRITICAL)
        elif name == "ERROR_SHELL":
            return 41
        else:
            logging.error("LOG level: '" + name + "' not defined")
            raise SystemExit()


    def _getLoggingFormat(self, enableColor: bool) -> str:
        format = "";
        if enableColor:
            format += "%(log_color)s"
        format += "[%(relativeCreated)d] - %(levelname)-13s"
        if enableColor:
            format += "%(reset)s"
        format += "%(message)s"
        return format


    def setupConsoleLogger(self, debugLevel: int) -> None:
        formatter = colorlog.ColoredFormatter(
            self._getLoggingFormat(True),
            log_colors={
                'DEBUG':       'cyan',
                'DEBUG_SHELL': 'yellow',
                'DEBUG_DIFF':  'blue',
                'INFO':        'green',
                'WARNING':     'yellow', # not used
                'ERROR':       'red',
                'ERROR_SHELL': 'purple',
                'CRITICAL':    'purple'  # not used
            }
        )

        logging.addLevelName(self.getCustomLogLevel('ERROR_SHELL'), 'ERROR_SHELL')
        logging.addLevelName(self.getCustomLogLevel('DEBUG_SHELL'), 'DEBUG_SHELL')
        logging.addLevelName(self.getCustomLogLevel('DEBUG_DIFF'), 'DEBUG_DIFF')

        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        streamHandler.setLevel(debugLevel)
        log = logging.getLogger()
        log.addHandler(streamHandler)
        log.setLevel(debugLevel)


    def setupFileLogger(self, fileName: str) -> None:
        formatter = logging.Formatter(self._getLoggingFormat(False))
        fileHandler = logging.FileHandler(fileName, 'w')
        fileHandler.setFormatter(formatter)
        log = logging.getLogger()
        log.addHandler(fileHandler)
        log.setLevel(logging.DEBUG)

