import server
from logzero import logger


def main():
    logger.info('Starting server')
    server.start_server()


if __name__ == '__main__':
    main()
