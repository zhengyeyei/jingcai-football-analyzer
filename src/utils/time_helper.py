"""时间处理助手"""
from datetime import datetime, timedelta
import pytz
from config.settings import config

class TimeHelper:
    """时间处理工具类"""
    
    TZ = pytz.timezone(config.TIMEZONE)
    
    @classmethod
    def now(cls):
        """获取当前时间（带时区）"""
        return datetime.now(cls.TZ)
    
    @classmethod
    def today(cls):
        """获取今天的日期"""
        return cls.now().date()
    
    @classmethod
    def parse_date(cls, date_str: str):
        """解析日期字符串"""
        try:
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            return None
    
    @classmethod
    def format_datetime(cls, dt: datetime, fmt: str = '%Y-%m-%d %H:%M:%S') -> str:
        """格式化时间"""
        return dt.strftime(fmt)
    
    @classmethod
    def is_match_day(cls, match_time: datetime) -> bool:
        """检查是否是比赛日"""
        return match_time.date() == cls.today()
    
    @classmethod
    def days_until_match(cls, match_time: datetime) -> int:
        """计算距离比赛还有多少天"""
        return (match_time.date() - cls.today()).days

time_helper = TimeHelper()
