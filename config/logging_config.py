"""日志配置"""
import os
from loguru import logger

def setup_logger():
    """配置日志系统"""
    from config.settings import config
    
    # 移除默认处理器
    logger.remove()
    
    # 添加控制台处理器
    logger.add(
        lambda msg: print(msg, end=''),
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>",
        level=config.LOG_LEVEL,
    )
    
    # 添加文件处理器
    os.makedirs(os.path.dirname(config.LOG_FILE) or '.', exist_ok=True)
    logger.add(
        config.LOG_FILE,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function} - {message}",
        level=config.LOG_LEVEL,
        rotation="500 MB",
        retention="10 days",
    )
    
    return logger

logger = setup_logger()
