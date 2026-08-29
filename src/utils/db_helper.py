"""数据库助手"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from config.settings import config
from src.utils.logger import logger

# 创建数据库引擎
engine = create_engine(config.DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class DBHelper:
    """数据库操作工具类"""
    
    @staticmethod
    def get_session() -> Session:
        """获取数据库会话"""
        return SessionLocal()
    
    @staticmethod
    def init_db():
        """初始化数据库"""
        try:
            Base.metadata.create_all(bind=engine)
            logger.info("数据库初始化成功")
        except Exception as e:
            logger.error(f"数据库初始化失败: {str(e)}")
            raise
    
    @staticmethod
    def drop_db():
        """删除所有表（仅用于开发）"""
        try:
            Base.metadata.drop_all(bind=engine)
            logger.warning("已删除所有数据库表")
        except Exception as e:
            logger.error(f"删除表失败: {str(e)}")
            raise

db_helper = DBHelper()
