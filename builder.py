#!/usr/bin/env python3

import sys
import traceback
import argparse
import logging
from datetime import datetime
from log import Log
from config.yamlParser import YamlParser
from config.example import Example
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


def builder(argv):
    args = parseArgs(argv)
    tasks.init()

    # setup logger
    log = Log()
    log.setupConsoleLogger(logging.DEBUG if args.debug else logging.INFO)
    if args.file:
        log.setupFileLogger(args.file)

    # display example configuration file
    if args.example:
        example = Example()
        for task in tasks.getTasks():
            example.addParameter(task.getTree())
        logging.info(example.getExampleConfig())
        return

    # parse config file and execute build
    if not args.config:
        return

    reportTime()
    parser = YamlParser(args.config)
    for task in tasks.getTasks():
        task.parseConfig(parser)
    for task in tasks.getTasks():
        task.execute()

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

