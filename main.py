import logging

logging.basicConfig(
    filename='example.log',
    format='%(asctime)s %(levelname)s %(name)s %(message)s'
)
logging.basicConfig(level=logging.DEBUG)


def log_to_file():
    logging.debug('Debug')
    logging.info('Info')
    logging.warning('Warning')
    logging.error('Error')
    logging.critical('Critical or Fatal')


if __name__ == '__main__':
    log_to_file()