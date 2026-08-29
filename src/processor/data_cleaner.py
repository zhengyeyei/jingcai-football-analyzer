"""数据清洗器"""
import pandas as pd
from typing import List, Dict, Any
from src.utils.logger import logger

class DataCleaner:
    """数据清洗工具类"""
    
    def __init__(self):
        self.logger = logger
    
    def clean_match_data(self, matches: List[Dict]) -> pd.DataFrame:
        """清洗比赛数据
        
        Args:
            matches: 原始比赛数据列表
        
        Returns:
            清洗后的DataFrame
        """
        self.logger.info(f"开始清洗{len(matches)}条比赛数据")
        
        df = pd.DataFrame(matches)
        
        # 移除重复数据
        df = df.drop_duplicates(subset=['id'])
        self.logger.info(f"移除重复数据后: {len(df)}条")
        
        # 检查必需列
        required_cols = ['id', 'home_team', 'away_team', 'start_time']
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            self.logger.warning(f"缺失列: {missing_cols}")
        
        # 数据类型转换
        if 'start_time' in df.columns:
            df['start_time'] = pd.to_datetime(df['start_time'])
        
        self.logger.info("数据清洗完成")
        return df
    
    def clean_odds_data(self, odds_data: List[Dict]) -> pd.DataFrame:
        """清洗赔率数据"""
        self.logger.info(f"开始清洗{len(odds_data)}条赔率数据")
        
        df = pd.DataFrame(odds_data)
        
        # 移除无效赔率
        if 'odds_sources' in df.columns:
            # 检查欧赔的有效性
            df = df[df['odds_sources'].apply(lambda x: x.get('european') is not None)]
        
        self.logger.info(f"清洗后: {len(df)}条")
        return df
    
    def handle_missing_values(self, df: pd.DataFrame, strategy: str = 'drop') -> pd.DataFrame:
        """处理缺失值
        
        Args:
            df: DataFrame
            strategy: 处理策略 ('drop'或'fill')
        
        Returns:
            处理后的DataFrame
        """
        missing_count = df.isnull().sum().sum()
        self.logger.info(f"检测到{missing_count}个缺失值")
        
        if strategy == 'drop':
            df = df.dropna()
        elif strategy == 'fill':
            df = df.fillna(0)
        
        self.logger.info(f"处理后: {len(df)}行")
        return df

data_cleaner = DataCleaner()
