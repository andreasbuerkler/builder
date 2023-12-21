#!/usr/bin/env python3

import sys
import traceback
from argparse import ArgumentParser
import logging
from log import Log
import config
import core
import parser
import tasks

def createArgumentParser() -> ArgumentParser:
    parser = ArgumentParser(description='The Great Builder')

    parser.add_argument("-v", action="version", version="0.1")
    parser.add_argument("-d", action="store_true", help="enable debug log to stdout", dest="debug")
    parser.add_argument("-e", action="store_true", help="display configuration file example", dest="example")
    parser.add_argument("-f", action="store", help="filename for logging", dest="file", type=str)
    parser.add_argument("-c", action="store", help="filename for configuration", dest="config", type=str)
    parser.add_argument("-l", action="store_true", help="show list of tasks", dest="list")

    return parser


def setupLogger(filePath: str, enableDebug: bool) -> None:
    log = Log()
    log.setupConsoleLogger(logging.DEBUG if enableDebug else logging.INFO)
    if filePath:
        log.setupFileLogger(filePath)


def builder(argv) -> int:
    flags = createArgumentParser()
    args = flags.parse_args(argv)
    setupLogger(args.file, args.debug)
    tasks.init()

    # display list of tasks
    if args.list:
        taskList: list[str] = core.getTaskSequence(tasks.getTasks())
        logging.info("Tasks: " + ", ".join(taskList))
        return 0

    # display example configuration file
    if args.example:
        message = "\n".ljust(80, "-") + config.getExampleConfig(tasks.getTasks()) + "\n".ljust(80, "-")
        logging.info("Example:" + message)
        return 0

    # apply configuration
    if args.config:
        config.transfer(tasks.getTasks(), parser.create(args.config))

    # execute build
    core.executeBuild(tasks.getTasks())
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

