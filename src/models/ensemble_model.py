"""集成模型"""
import pandas as pd
import numpy as np
from typing import Dict, List
from src.models.base_model import BaseModel
from src.models.poisson_model import poisson_model
from src.models.ml_model import ml_model

class EnsembleModel(BaseModel):
    """集成预测模型
    
    结合Poisson模型和ML模型的预测结果
    """
    
    def __init__(self):
        super().__init__('Ensemble')
        self.poisson = poisson_model
        self.ml = ml_model
        self.weights = {'poisson': 0.4, 'ml': 0.6}  # 模型权重
    
    def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> None:
        """训练集成模型"""
        self.logger.info("开始训练集成模型")
        
        # 训练Poisson模型
        self.poisson.train(X_train, y_train)
        
        # 训练ML模型
        self.ml.train(X_train, y_train)
        
        self.is_trained = True
        self.logger.info("集成模型训练完成")
    
    def predict(self, features: pd.DataFrame) -> List[Dict]:
        """进行集成预测"""
        if not self.is_trained:
            self.logger.error("模型未训练")
            return []
        
        self.logger.info(f"对{len(features)}场比赛进行集成预测")
        
        # 获取各模型的预测
        poisson_preds = self.poisson.predict(features)
        ml_preds = self.ml.predict(features)
        
        # 融合预测
        ensemble_preds = []
        
        for i in range(len(features)):
            match_data = features.iloc[i]
            p_pred = poisson_preds[i] if i < len(poisson_preds) else {}
            m_pred = ml_preds[i] if i < len(ml_preds) else {}
            
            # 加权平均
            win_prob = (p_pred.get('win_prob', 0) * self.weights['poisson'] + 
                       m_pred.get('win_prob', 0) * self.weights['ml'])
            draw_prob = (p_pred.get('draw_prob', 0) * self.weights['poisson'] + 
                        m_pred.get('draw_prob', 0) * self.weights['ml'])
            loss_prob = (p_pred.get('loss_prob', 0) * self.weights['poisson'] + 
                        m_pred.get('loss_prob', 0) * self.weights['ml'])
            
            # 正规化
            total = win_prob + draw_prob + loss_prob
            if total > 0:
                win_prob /= total
                draw_prob /= total
                loss_prob /= total
            
            # 确定推荐
            max_prob = max(win_prob, draw_prob, loss_prob)
            if max_prob == win_prob:
                recommendation = '胜'
            elif max_prob == draw_prob:
                recommendation = '平'
            else:
                recommendation = '负'
            
            prediction = {
                'match_id': match_data.get('match_id', f'match_{i}'),
                'home_team': match_data.get('home_team', ''),
                'away_team': match_data.get('away_team', ''),
                'win_prob': win_prob,
                'draw_prob': draw_prob,
                'loss_prob': loss_prob,
                'recommendation': recommendation,
                'confidence': max_prob,
                'odds': {
                    'win': match_data.get('home_odds', 1.8),
                    'draw': match_data.get('draw_odds', 3.5),
                    'loss': match_data.get('away_odds', 4.2)
                },
                'model': 'Ensemble'
            }
            
            ensemble_preds.append(prediction)
        
        return ensemble_preds

ensemble_model = EnsembleModel()
