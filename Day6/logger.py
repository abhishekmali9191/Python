import logging
logging.basicConfig(
    filename= 'basicConfig.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

logger = logging.getLogger('advancedConfig_logger')
handler = logging.FileHandler('advancedConfig.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler,)
logger.setLevel(logging.DEBUG)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')



#----------------------------------------------------------------
# output 
# WARNING:root:This is a warning message
# ERROR:root:This is an error message
# CRITICAL:root:This is a critical message
# DEBUG:advancedConfig_logger:This is a debug message
# INFO:advancedConfig_logger:This is an info message
# WARNING:advancedConfig_logger:This is a warning message
# ERROR:advancedConfig_logger:This is an error message
# CRITICAL:advancedConfig_logger:This is a critical message