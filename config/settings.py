"""配置管理模块"""
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """全局配置类"""
    
    # 数据库配置
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./data/football.db')
    
    # API配置
    API_HOST = os.getenv('API_HOST', '0.0.0.0')
    API_PORT = int(os.getenv('API_PORT', 8000))
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    
    # 爬虫配置
    MATCH_DATA_SOURCE = os.getenv('MATCH_DATA_SOURCE', 'https://api.sports.com/matches')
    ODDS_DATA_SOURCE = os.getenv('ODDS_DATA_SOURCE', 'https://api.odds.com/odds')
    CRAWL_DELAY = int(os.getenv('CRAWL_DELAY', 2))
    CRAWL_TIMEOUT = int(os.getenv('CRAWL_TIMEOUT', 10))
    
    # 模型配置
    MODEL_TYPE = os.getenv('MODEL_TYPE', 'ensemble')
    XGB_MAX_DEPTH = int(os.getenv('XGB_MAX_DEPTH', 6))
    XGB_LEARNING_RATE = float(os.getenv('XGB_LEARNING_RATE', 0.1))
    XGB_N_ESTIMATORS = int(os.getenv('XGB_N_ESTIMATORS', 100))
    
    # 投注策略配置
    INITIAL_BANKROLL = float(os.getenv('INITIAL_BANKROLL', 10000))
    KELLY_FRACTION = float(os.getenv('KELLY_FRACTION', 0.25))
    MIN_ODDS = float(os.getenv('MIN_ODDS', 1.5))
    MAX_ODDS = float(os.getenv('MAX_ODDS', 10.0))
    
    # 日志配置
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'logs/app.log')
    
    # 其他配置
    TIMEZONE = os.getenv('TIMEZONE', 'Asia/Shanghai')
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-in-production')

config = Config()
