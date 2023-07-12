import logging

class CustomFormatter(logging.Formatter):
    def format(self, record):
        log_format = "[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s"
        formatter = logging.Formatter(log_format, datefmt='%Y-%m-%d %H:%M:%S')

        return formatter.format(record)

class StdoutHandler(logging.Handler):
    def __init__(self):
        super().__init__()

    def emit(self, record):
        log_entry = self.format(record)
        print(log_entry)

class LoggerHandler():
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.loggerHandler = StdoutHandler()
        self.formatter = CustomFormatter()
        self.loggerHandler.setFormatter(self.formatter)
        self.logger.addHandler(self.loggerHandler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

logger = LoggerHandler()