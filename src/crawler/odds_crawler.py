"""赔率数据爬虫"""
from typing import List, Dict, Any
from src.utils.logger import logger
from src.utils.http_helper import http_helper

class OddsCrawler:
    """赔率数据爬虫"""
    
    def __init__(self):
        self.logger = logger
    
    def fetch_odds_for_matches(self, matches: List[Dict]) -> List[Dict[str, Any]]:
        """为比赛列表获取赔率数据
        
        Args:
            matches: 比赛数据列表
        
        Returns:
            赔率数据列表
        """
        self.logger.info(f"开始爬取{len(matches)}场比赛的赔率数据")
        
        odds_list = []
        for match in matches:
            odds = self._get_odds_for_match(match)
            odds_list.append(odds)
        
        self.logger.info(f"成功获取{len(odds_list)}条赔率数据")
        return odds_list
    
    def _get_odds_for_match(self, match: Dict) -> Dict[str, Any]:
        """获取单场比赛的赔率数据"""
        return {
            'match_id': match['id'],
            'home_team': match['home_team'],
            'away_team': match['away_team'],
            'odds_sources': {
                'european': {
                    'win': match['odds']['win'],
                    'draw': match['odds']['draw'],
                    'loss': match['odds']['loss']
                },
                'asian': {
                    'handicap': 0.5,
                    'odds': 1.90
                },
                'total_goals': {
                    'over_2_5': 1.85,
                    'under_2_5': 1.95
                }
            },
            'max_odds': max(match['odds']['win'], match['odds']['draw'], match['odds']['loss']),
            'min_odds': min(match['odds']['win'], match['odds']['draw'], match['odds']['loss'])
        }
    
    def fetch_odds_history(self, match_id: str, days: int = 7) -> List[Dict[str, Any]]:
        """获取赔率历史数据
        
        Args:
            match_id: 比赛ID
            days: 查询天数
        
        Returns:
            赔率历史列表
        """
        self.logger.info(f"爬取比赛{match_id}的{days}天赔率历史")
        
        # 模拟数据
        history = [
            {'day': i, 'win_odds': 1.8 - (i * 0.02), 'draw_odds': 3.5, 'loss_odds': 4.2 + (i * 0.05)}
            for i in range(days)
        ]
        
        return history

odds_crawler = OddsCrawler()
