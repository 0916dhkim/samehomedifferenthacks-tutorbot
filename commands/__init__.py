# commands package
from .busy import busy
from .free import free
from .register import register
from .sos import sos
from .status import status
from .unregister import unregister
import logging


def add_commands():
    logging.info("Commands are added.")


__all__ = [
    "busy",
    "free",
    "register",
    "unregister",
    "sos",
    "status",
    "unregister",
    "wisdom"
]
