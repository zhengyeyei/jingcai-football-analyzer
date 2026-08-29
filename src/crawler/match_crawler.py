"""比赛数据爬虫"""
from typing import List, Dict, Any
from datetime import datetime, timedelta
from src.utils.logger import logger
from src.utils.http_helper import http_helper
from src.utils.time_helper import time_helper
import json

class MatchCrawler:
    """比赛数据爬虫"""
    
    def __init__(self):
        self.logger = logger
    
    def fetch_upcoming_matches(self, days_ahead: int = 7) -> List[Dict[str, Any]]:
        """获取即将进行的比赛数据
        
        Args:
            days_ahead: 提前多少天获取数据，默认7天
        
        Returns:
            比赛数据列表
        """
        self.logger.info(f"开始爬取{days_ahead}天内的比赛数据")
        
        # 这里是示例数据，实际应连接真实API
        matches = self._get_mock_matches(days_ahead)
        
        self.logger.info(f"成功获取{len(matches)}场比赛数据")
        return matches
    
    def _get_mock_matches(self, days_ahead: int) -> List[Dict[str, Any]]:
        """获取模拟数据（用于演示）"""
        teams = [
            ('阿森纳', '曼联'),
            ('曼城', '利物浦'),
            ('切尔西', '托特纳姆'),
            ('曼联', '埃弗顿'),
            ('利物浦', '阿斯顿维拉'),
        ]
        
        matches = []
        base_time = time_helper.now()
        
        for i, (home, away) in enumerate(teams[:days_ahead]):
            match_time = base_time + timedelta(days=i, hours=20)
            match = {
                'id': f'match_{i:03d}',
                'home_team': home,
                'away_team': away,
                'start_time': match_time.isoformat(),
                'league': 'Premier League',
                'status': 'upcoming',
                'odds': {
                    'win': round(1.5 + (i * 0.1), 2),
                    'draw': round(3.5 + (i * 0.05), 2),
                    'loss': round(4.0 + (i * 0.1), 2)
                }
            }
            matches.append(match)
        
        return matches
    
    def fetch_finished_matches(self, date_str: str = None) -> List[Dict[str, Any]]:
        """获取已完成的比赛数据
        
        Args:
            date_str: 日期字符串 (YYYY-MM-DD)
        
        Returns:
            已完成的比赛数据列表
        """
        if date_str is None:
            date_str = time_helper.format_datetime(time_helper.today(), '%Y-%m-%d')
        
        self.logger.info(f"爬取{date_str}的已完成比赛数据")
        
        # 模拟数据
        finished_matches = [
            {
                'id': 'match_finished_001',
                'home_team': '曼城',
                'away_team': '布赖顿',
                'final_score': '3:1',
                'home_goals': 3,
                'away_goals': 1,
                'date': date_str,
                'league': 'Premier League'
            }
        ]
        
        return finished_matches

match_crawler = MatchCrawler()
