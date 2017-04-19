#!/usr/bin/env python
"""
Looger to use in all modules
"""
import os
import logging
import logging.handlers

LOG_FILE='/tmp/decision_engine_logs/decision_engine_log'
MB=000000
ROTATE_AFTER = 6

def set_logging(log_file_name=LOG_FILE, max_file_size= 200*MB, max_backup_count = ROTATE_AFTER):
    """

    :type log_file_name: :obj:`str`
    :arg log_file_name: log file name
    :type  max_file_size: :obj:`int`
    :arg  max_file_size: maximal size of log file. If reached save and start new log.
    :type  max_backup_count: :obj:`int`
    :arg  max_backup_count: start rotaion after this number is reached
    :rtype: :class:`logging.Logger` - rotating file logger
    """
    if not os.path.exists(os.path.dirname(log_file_name)):
        os.makedirs(os.path.dirname(log_file_name))
    logger =  logging.getLogger("decision_engine")
    #logger =  logging.getLogger()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s")

    handler = logging.handlers.RotatingFileHandler(log_file_name,
                                                   maxBytes=max_file_size,
                                                   backupCount=max_backup_count)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.setLevel(logging.INFO)
    #logger.setLevel(logging.DEBUG)
    #logger =  logging.getLogger(__name__)

    return logger

def set_stream_logging(logger_name=''):
    """
    This is for debugging.
    Set stream logging for logger.

    :type logger_name: :obj:`str`
    :arg logger_name: logger name
    :rtype: :class:`logging.Logger`
    """

    logger =  logging.getLogger("decision_engine")
    #logger =  logging.getLogger()
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(module)s - %(levelname)s - %(message)s")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.setLevel(logging.INFO)
    #logger.setLevel(logging.DEBUG)
    #logger =  logging.getLogger(__name__)

    return logger

