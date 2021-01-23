from src.util.FileIO import FileIO

import logging
import sys
import os

class LogFactory():
    loggers: {} = {}
    log_dir: str = ''
    log_level: str = 'DEBUG'
    log_stdout: bool = True
    MAIN_LOG: logging._loggerClass

    @staticmethod
    def get_logger(logName: str, stdOutOnly: bool = False) -> logging._loggerClass:
        if LogFactory.log_dir != '' and  not os.path.exists(LogFactory.log_dir):
            os.makedirs(LogFactory.log_dir)

        if logName not in LogFactory.loggers:
            FileIO.create_file_if_does_not_exist(f"{LogFactory.log_dir}{os.sep}{logName}.log")

            LogFactory.loggers[logName] = logging.getLogger(logName)
            LogFactory.loggers[logName].setLevel(logging.getLevelName(LogFactory.log_level))
            formatter: logging.Formatter = logging.Formatter('[%(asctime)s %(levelname)s]: %(message)s')
            if not stdOutOnly:
              handler: logging.FileHandler=logging.FileHandler(f"{LogFactory.log_dir}{os.sep}{logName}.log", encoding='utf-8')
              handler.setFormatter(formatter)
              LogFactory.loggers[logName].addHandler(handler)

            # create console handler with a higher log level
            if LogFactory.log_stdout:
                stdhandler = logging.StreamHandler(sys.stdout)
                stdhandler.setLevel(logging.getLevelName(LogFactory.log_level))
                stdhandler.setFormatter(formatter)
                LogFactory.loggers[logName].addHandler(stdhandler)

        return LogFactory.loggers[logName]

    @staticmethod
    def touch_file(path):
        with open(path, 'w+'):
            os.utime(path, None)

    @staticmethod
    def main_log():
        LogFactory.MAIN_LOG = LogFactory.get_logger(f"main", stdOutOnly=True)
        LogFactory.MAIN_LOG .info('=====   MAIN LOGGER STARTED     =====')