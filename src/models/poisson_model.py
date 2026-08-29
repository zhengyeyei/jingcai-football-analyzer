"""Poisson分布模型"""
import numpy as np
from scipy.stats import poisson
from scipy.special import comb
import pandas as pd
from typing import Dict, Tuple
from src.models.base_model import BaseModel
from src.utils.logger import logger

class PoissonModel(BaseModel):
    """Poisson分布预测模型"""
    
    def __init__(self):
        super().__init__('Poisson')
        self.home_attack = None
        self.home_defense = None
        self.away_attack = None
        self.away_defense = None
        self.avg_home_goals = None
        self.avg_away_goals = None
    
    def train(self, X_train: pd.DataFrame, y_train: pd.Series = None) -> None:
        """训练Poisson模型
        
        使用历史数据计算Poisson参数
        """
        self.logger.info("开始训练Poisson模型")
        
        # 模拟计算（实际应使用真实数据）
        self.avg_home_goals = 1.5
        self.avg_away_goals = 1.0
        self.home_attack = 1.3
        self.home_defense = 0.8
        self.away_attack = 0.9
        self.away_defense = 1.1
        
        self.is_trained = True
        self.logger.info("Poisson模型训练完成")
    
    def predict(self, features: pd.DataFrame) -> Dict:
        """使用Poisson分布预测"""
        if not self.is_trained:
            self.logger.error("模型未训练")
            return {}
        
        self.logger.info(f"对{len(features)}场比赛进行Poisson预测")
        
        predictions = []
        
        for idx, row in features.iterrows():
            # 计算预期进球数
            home_lambda = self.avg_home_goals * row.get('home_strength', 1.5)
            away_lambda = self.avg_away_goals * row.get('away_strength', 1.0)
            
            # 计算每个比分的概率
            probs = {}
            total_prob_home = 0
            total_prob_draw = 0
            total_prob_away = 0
            
            for h_goals in range(6):
                for a_goals in range(6):
                    prob = poisson.pmf(h_goals, home_lambda) * poisson.pmf(a_goals, away_lambda)
                    
                    if h_goals > a_goals:
                        total_prob_home += prob
                    elif h_goals == a_goals:
                        total_prob_draw += prob
                    else:
                        total_prob_away += prob
            
            predictions.append({
                'match_id': row.get('match_id', f'match_{idx}'),
                'home_team': row.get('home_team', ''),
                'away_team': row.get('away_team', ''),
                'win_prob': total_prob_home,
                'draw_prob': total_prob_draw,
                'loss_prob': total_prob_away,
                'expected_home_goals': home_lambda,
                'expected_away_goals': away_lambda,
                'model': 'Poisson'
            })
        
        return predictions
    
    def get_score_probabilities(self, home_lambda: float, away_lambda: float, max_goals: int = 5) -> Dict:
        """获取各个比分的概率分布"""
        score_probs = {}
        
        for h in range(max_goals):
            for a in range(max_goals):
                score = f"{h}-{a}"
                prob = poisson.pmf(h, home_lambda) * poisson.pmf(a, away_lambda)
                score_probs[score] = prob
        
        return score_probs

poisson_model = PoissonModel()
