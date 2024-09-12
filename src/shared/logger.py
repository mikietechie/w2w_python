"""
Desc: Logging Conf
"""

import logging

logging.basicConfig(
    filename="process.log",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)

logging.info("Running Urban Planning")

logger = logging.getLogger("TGBOT")
