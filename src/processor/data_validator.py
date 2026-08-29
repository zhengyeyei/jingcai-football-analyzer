"""数据验证器"""
import pandas as pd
from typing import List, Dict, Tuple
from src.utils.logger import logger

class DataValidator:
    """数据验证工具类"""
    
    def __init__(self):
        self.logger = logger
    
    def validate_matches(self, matches: List[Dict]) -> Tuple[bool, List[str]]:
        """验证比赛数据的完整性和正确性
        
        Returns:
            (是否有效, 错误列表)
        """
        errors = []
        
        if not matches:
            errors.append("比赛数据为空")
            return False, errors
        
        required_fields = ['id', 'home_team', 'away_team', 'start_time']
        
        for i, match in enumerate(matches):
            # 检查必需字段
            for field in required_fields:
                if field not in match:
                    errors.append(f"比赛{i}: 缺少字段 {field}")
            
            # 检查赔率有效性
            if 'odds' in match:
                odds = match['odds']
                if isinstance(odds, dict):
                    for key in ['win', 'draw', 'loss']:
                        if key not in odds or odds[key] <= 0:
                            errors.append(f"比赛{i}: 无效的{key}赔率")
        
        valid = len(errors) == 0
        if valid:
            self.logger.info(f"验证通过: {len(matches)}场比赛")
        else:
            self.logger.warning(f"验证失败: {len(errors)}个错误")
        
        return valid, errors
    
    def validate_odds(self, odds_data: List[Dict]) -> Tuple[bool, List[str]]:
        """验证赔率数据"""
        errors = []
        
        for i, odds in enumerate(odds_data):
            # 检查赔率合理性（三向赔率之和应该小于等于1）
            if 'odds_sources' in odds and 'european' in odds['odds_sources']:
                euro_odds = odds['odds_sources']['european']
                if all(k in euro_odds for k in ['win', 'draw', 'loss']):
                    implied_probs_sum = 1/euro_odds['win'] + 1/euro_odds['draw'] + 1/euro_odds['loss']
                    if implied_probs_sum > 1.05:  # 允许5%的误差
                        errors.append(f"赔率{i}: 隐含概率之和过高 ({implied_probs_sum:.2%})")
        
        valid = len(errors) == 0
        return valid, errors

data_validator = DataValidator()
