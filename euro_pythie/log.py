from datetime import date
import logging

class CustomFormatter(logging.Formatter):
    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    format = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(CustomFormatter())

file_handler = logging.FileHandler('log/europythie_{}.log'.format(date.today().strftime('%Y_%m_%d')))
file_handler.setLevel(level=logging.DEBUG)
file_handler.setFormatter(CustomFormatter())

logging.basicConfig(
    encoding="utf-8",
    format="%(asctime)s %(levelname)s: %(message)s",
    level=logging.DEBUG,
    handlers=[consoleHandler, file_handler],
)
main = logging.getLogger("Euro_pythie")
command = logging.getLogger("Game_command")
database = logging.getLogger("Database")