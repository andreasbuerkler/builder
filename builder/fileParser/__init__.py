import os
import logging
from builder.fileParser.factory import Factory
from builder.fileParser.Iparser import IParser

def create(configFilePath: str) -> IParser:
    if not os.path.isfile(configFilePath):
        logging.error("Config file does not exist")
        raise SystemExit()

    return Factory(configFilePath)
