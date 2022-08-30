#!/usr/bin/env python3

__author__ = 'Amal Rajan'
__version__ = '0.1.0'
__license__ = 'MIT'

from logzero import logger
from server import start_server


def main():
    logger.info('Starting server')
    start_server()

if __name__ == '__main__':
    main()
