import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='example_logs.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S')

logging.debug('Log de debugging')
logging.info('Log informativo')
logging.warning('Log de advertencia')
logging.error('Log de error')
logging.critical('Log de error critico')

try:
    division = 2/0
except:
    logging.exception('Division por 0')