"""机器学习模型"""
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder
from typing import Dict, List
from src.models.base_model import BaseModel
from config.settings import config

class MLModel(BaseModel):
    """机器学习预测模型（基于XGBoost）"""
    
    def __init__(self):
        super().__init__('XGBoost')
        self.model = XGBClassifier(
            max_depth=config.XGB_MAX_DEPTH,
            learning_rate=config.XGB_LEARNING_RATE,
            n_estimators=config.XGB_N_ESTIMATORS,
            random_state=42,
            eval_metric='mlogloss'
        )
        self.label_encoders = {}
    
    def _prepare_features(self, X: pd.DataFrame) -> pd.DataFrame:
        """准备特征数据"""
        X = X.copy()
        
        # 编码字符串列
        for col in ['home_team', 'away_team']:
            if col in X.columns and X[col].dtype == 'object':
                if col not in self.label_encoders:
                    self.label_encoders[col] = LabelEncoder()
                    X[col] = self.label_encoders[col].fit_transform(X[col])
                else:
                    X[col] = self.label_encoders[col].transform(X[col])
        
        # 只保留数值特征
        X = X.select_dtypes(include=[np.number])
        return X
    
    def train(self, X_train: pd.DataFrame, y_train: pd.Series) -> None:
        """训练XGBoost模型"""
        self.logger.info("开始训练XGBoost模型")
        
        X = self._prepare_features(X_train)
        
        self.model.fit(
            X, y_train,
            verbose=False
        )
        
        self.is_trained = True
        self.logger.info("XGBoost模型训练完成")
    
    def predict(self, features: pd.DataFrame) -> List[Dict]:
        """进行预测"""
        if not self.is_trained:
            self.logger.error("模型未训练")
            return []
        
        self.logger.info(f"对{len(features)}场比赛进行XGBoost预测")
        
        X = self._prepare_features(features)
        
        # 获取预测概率
        probs = self.model.predict_proba(X)
        
        predictions = []
        for i in range(len(features)):
            match_data = features.iloc[i]
            prediction = {
                'match_id': match_data.get('match_id', f'match_{i}'),
                'home_team': match_data.get('home_team', ''),
                'away_team': match_data.get('away_team', ''),
                'win_prob': probs[i][0] if probs.shape[1] > 0 else 0,
                'draw_prob': probs[i][1] if probs.shape[1] > 1 else 0,
                'loss_prob': probs[i][2] if probs.shape[1] > 2 else 0,
                'model': 'XGBoost'
            }
            predictions.append(prediction)
        
        return predictions

ml_model = MLModel()
