from abc import ABC , abstractmethod
from enum import Enum
import time
class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    ERROR = 3

class LogMessage:
    def __init__(self , level:LogLevel , message : str):
        self.level = level
        self.message = message
        self.timestamp = int(time.time())

class LoggerInterface(ABC):
    
    @abstractmethod
    def append(self , message : LogMessage):
        pass

class ConsoleLogger(LoggerInterface):
    
    def append(self, message: LogMessage):
        print(message)

class FileLogger(LoggerInterface):
    
    def __init__(self , path):
        self.path = path
    
    def append(self, message:LogMessage):
        with open(self.path, "a") as file:
            file.write(message)


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._handlers = []  # List to store logger interface objects.
        return cls._instance

    def register_handler(self, handler: LoggerInterface):
        self._handlers.append(handler)

    def log(self, level: LogLevel, message: str):
        log_msg = LogMessage(level, message)
        for handler in self._handlers:
            handler.append(log_msg)