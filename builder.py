#!/usr/bin/env python3

import sys
import traceback
import argparse
import logging
from datetime import datetime
from log import Log
from core.yamlParser import YamlParser
from core.example import Example
import tasks

def parseArgs(argv):
    parser = argparse.ArgumentParser(description='The Great Builder')

    parser.add_argument('-v', action="version", version="0.1")
    parser.add_argument('-d', action="store_true", help="enable debug log to stdout", dest="debug")
    parser.add_argument('-e', action="store_true", help="display configuration file example", dest="example")
    parser.add_argument('-f', action="store", help="filename for logging", dest="file", type=str)
    parser.add_argument('-c', action="store", help="filename for configuration", dest="config", type=str)

    return parser.parse_args(argv)


def reportTime():
    now = datetime.now()
    timeString = now.strftime("%d.%m.%Y %H:%M:%S")
    logging.info("Build date and time: " + timeString)


def setupLogger(enableDebug: bool, filePath: str):
    log = Log()
    log.setupConsoleLogger(logging.DEBUG if enableDebug else logging.INFO)
    if filePath:
        log.setupFileLogger(filePath)


def showExampleConfig():
    tasks.init()
    example = Example()
    for task in tasks.getTasks():
        example.addParameterList(task.getList())
    logging.info(example.getExampleConfig())


def executeBuild(configFilePath: str):
    tasks.init()
    parser = YamlParser(configFilePath)
    for task in tasks.getTasks():
        task.parseConfig(parser)
    for task in tasks.getTasks():
        task.execute()


def builder(argv):
    args = parseArgs(argv)
    setupLogger(args.debug, args.file)

    # display example configuration file
    if args.example:
        showExampleConfig()
        return

    # parse config file and execute build
    if args.config:
        reportTime()
        executeBuild(args.config)

    logging.info("Build completed")


def main():
    try:
        sys.exit(builder(sys.argv[1:]))
    except Exception as err:
        logging.error('%s', err)
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

