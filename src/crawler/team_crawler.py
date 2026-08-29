"""球队信息爬虫"""
from typing import List, Dict, Any
from src.utils.logger import logger

class TeamCrawler:
    """球队信息爬虫"""
    
    def __init__(self):
        self.logger = logger
        self.teams_cache = {}
    
    def fetch_team_info(self, team_name: str) -> Dict[str, Any]:
        """获取球队信息
        
        Args:
            team_name: 球队名称
        
        Returns:
            球队信息字典
        """
        if team_name in self.teams_cache:
            return self.teams_cache[team_name]
        
        self.logger.info(f"爬取球队信息: {team_name}")
        
        team_info = self._get_mock_team_info(team_name)
        self.teams_cache[team_name] = team_info
        
        return team_info
    
    def _get_mock_team_info(self, team_name: str) -> Dict[str, Any]:
        """获取模拟球队信息"""
        team_data = {
            '曼城': {
                'rank': 1,
                'total_matches': 30,
                'wins': 25,
                'draws': 3,
                'losses': 2,
                'goals_for': 85,
                'goals_against': 18,
                'goal_difference': 67,
                'points': 78
            },
            '阿森纳': {
                'rank': 2,
                'total_matches': 30,
                'wins': 23,
                'draws': 4,
                'losses': 3,
                'goals_for': 78,
                'goals_against': 25,
                'goal_difference': 53,
                'points': 73
            },
            '利物浦': {
                'rank': 3,
                'total_matches': 30,
                'wins': 22,
                'draws': 5,
                'losses': 3,
                'goals_for': 75,
                'goals_against': 28,
                'goal_difference': 47,
                'points': 71
            }
        }
        
        return team_data.get(team_name, {
            'rank': 'N/A',
            'total_matches': 0,
            'wins': 0,
            'draws': 0,
            'losses': 0,
            'goals_for': 0,
            'goals_against': 0,
            'goal_difference': 0,
            'points': 0
        })
    
    def fetch_recent_form(self, team_name: str, matches: int = 5) -> List[str]:
        """获取球队近期战绩
        
        Args:
            team_name: 球队名称
            matches: 查看最近多少场比赛
        
        Returns:
            近期战绩列表（'W'=胜，'D'=平，'L'=负）
        """
        self.logger.info(f"获取{team_name}的近{matches}场战绩")
        
        # 模拟数据：W表示胜，D表示平，L表示负
        form_map = {
            '曼城': ['W', 'W', 'D', 'W', 'W'],
            '阿森纳': ['W', 'W', 'W', 'D', 'W'],
            '利物浦': ['W', 'D', 'W', 'W', 'D'],
        }
        
        return form_map.get(team_name, [])

team_crawler = TeamCrawler()
