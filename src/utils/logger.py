"""日志工具"""
from config.logging_config import logger

class Logger:
    """日志包装器"""
    
    @staticmethod
    def info(msg):
        logger.info(msg)
    
    @staticmethod
    def error(msg, exc_info=False):
        logger.error(msg)
    
    @staticmethod
    def warning(msg):
        logger.warning(msg)
    
    @staticmethod
    def debug(msg):
        logger.debug(msg)

__all__ = ['Logger', 'logger']
