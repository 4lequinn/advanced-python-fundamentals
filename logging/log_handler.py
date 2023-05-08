import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
format_log = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(format_log)
logger.addHandler(console_handler)

file_handler = logging.FileHandler('file.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(format_log)
logger.addHandler(file_handler)


logger.info('Registro informativo')