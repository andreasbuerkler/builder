#!/usr/bin/env python3

import sys
import traceback
import argparse
import logging
from log import Log
import core
import tasks

def parseArgs(argv) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='The Great Builder')

    parser.add_argument('-v', action="version", version="0.1")
    parser.add_argument('-d', action="store_true", help="enable debug log to stdout", dest="debug")
    parser.add_argument('-e', action="store_true", help="display configuration file example", dest="example")
    parser.add_argument('-f', action="store", help="filename for logging", dest="file", type=str)
    parser.add_argument('-c', action="store", help="filename for configuration", dest="config", type=str)

    return parser.parse_args(argv)


def setupLogger(filePath: str, enableDebug: bool) -> None:
    log = Log()
    log.setupConsoleLogger(logging.DEBUG if enableDebug else logging.INFO)
    if filePath:
        log.setupFileLogger(filePath)


def builder(argv) -> int:
    args = parseArgs(argv)
    setupLogger(args.file, args.debug)

    if args.config:
        core.configure(args.config)

    tasks.init()
    for task in tasks.getTasks():
        core.addTask(task)

    # display example configuration file
    if args.example:
        logging.info(core.getExampleConfig())
        return 0

    # execute build
    core.executeBuild()
    return 0


def main() -> None:
    try:
        sys.exit(builder(sys.argv[1:]))
    except Exception as err:
        logging.error('%s', err)
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

