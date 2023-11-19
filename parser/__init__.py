import os
import logging
from parser.builder import Builder
from parser.Iparser import IParser

def create(configFilePath: str) -> IParser:
    if os.path.isfile(configFilePath) == False:
        logging.error("Config file does not exist")
        raise SystemExit()

    return Builder(configFilePath)

