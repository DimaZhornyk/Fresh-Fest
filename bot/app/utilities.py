import logging

from .config import LOG_FILE


def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        filename=LOG_FILE,
                        filemode='a')
