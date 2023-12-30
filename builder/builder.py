import sys
import traceback
from argparse import ArgumentParser
import logging
import builder.config
import builder.core
import builder.fileParser
import builder.tasks
from builder.log import Log

def _createArgumentParser() -> ArgumentParser:
    argumentParser = ArgumentParser(description='The Great Builder')

    argumentParser.add_argument("-v", action="version", version="0.1")
    argumentParser.add_argument("-d", action="store_true", help="enable debug log to stdout", dest="debug")
    argumentParser.add_argument("-e", action="store_true", help="display configuration file example", dest="example")
    argumentParser.add_argument("-f", action="store", help="filename for logging", dest="file", type=str)
    argumentParser.add_argument("-c", action="store", help="filename for configuration", dest="config", type=str)
    argumentParser.add_argument("-l", action="store_true", help="show list of tasks", dest="list")

    return argumentParser


def _setupLogger(filePath: str, enableDebug: bool) -> None:
    log = Log()
    log.setupConsoleLogger(logging.DEBUG if enableDebug else logging.INFO)
    if filePath:
        log.setupFileLogger(filePath)


def _build(argv) -> int:
    flags = _createArgumentParser()
    args = flags.parse_args(argv)
    _setupLogger(args.file, args.debug)
    builder.tasks.init()
    builder.tasks.setTasks(builder.core.sort(builder.tasks.getTasks()))

    # display list of tasks
    if args.list:
        taskList: list[str] = builder.core.getTaskSequence(builder.tasks.getTasks())
        logging.info("Tasks: " + ", ".join(taskList))
        return 0

    # display example configuration file
    if args.example:
        message = "\n".ljust(80, "-") + builder.config.getExampleConfig(builder.tasks.getTasks()) + "\n".ljust(80, "-")
        logging.info("Example:" + message)
        return 0

    # apply configuration
    if args.config:
        builder.config.transfer(builder.tasks.getTasks(), builder.fileParser.create(args.config))

    # execute build
    builder.tasks.executeBuild()
    return 0


def main() -> None:
    try:
        sys.exit(_build(sys.argv[1:]))
    except Exception as err:
        logging.error('%s', err)
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
