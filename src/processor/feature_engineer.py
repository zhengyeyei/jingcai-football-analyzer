"""特征工程"""
import pandas as pd
import numpy as np
from typing import List, Dict, Any
from src.utils.logger import logger

class FeatureEngineer:
    """特征工程工具类"""
    
    def __init__(self):
        self.logger = logger
    
    def extract_features(self, matches: List[Dict], team_stats: Dict = None) -> pd.DataFrame:
        """从比赛数据中提取特征
        
        Args:
            matches: 比赛数据列表
            team_stats: 球队统计数据
        
        Returns:
            特征DataFrame
        """
        self.logger.info("开始特征提取")
        
        df = pd.DataFrame(matches)
        features = pd.DataFrame()
        
        # 基础特征
        features['match_id'] = df['id']
        features['home_team'] = df['home_team']
        features['away_team'] = df['away_team']
        
        # 赔率相关特征
        if 'odds' in df.columns:
            features['home_odds'] = df['odds'].apply(lambda x: x.get('win', 0) if isinstance(x, dict) else 0)
            features['draw_odds'] = df['odds'].apply(lambda x: x.get('draw', 0) if isinstance(x, dict) else 0)
            features['away_odds'] = df['odds'].apply(lambda x: x.get('loss', 0) if isinstance(x, dict) else 0)
            
            # 隐含概率
            features['home_prob'] = 1 / features['home_odds']
            features['draw_prob'] = 1 / features['draw_odds']
            features['away_prob'] = 1 / features['away_odds']
        
        # 模拟的球队实力特征
        features['home_strength'] = np.random.uniform(6, 9, len(features))
        features['away_strength'] = np.random.uniform(5, 8.5, len(features))
        
        # 主客优势
        features['home_advantage'] = features['home_strength'] - features['away_strength']
        
        # 交手历史特征（模拟）
        features['head_to_head_home_wins'] = np.random.randint(0, 5, len(features))
        features['head_to_head_draws'] = np.random.randint(0, 4, len(features))
        features['head_to_head_away_wins'] = np.random.randint(0, 5, len(features))
        
        self.logger.info(f"特征提取完成，生成{len(features)}条特征，维度: {features.shape[1]}")
        return features
    
    def create_target_variable(self, matches_with_results: List[Dict]) -> pd.Series:
        """创建目标变量（比赛结果）
        
        Args:
            matches_with_results: 包含比赛结果的比赛数据
        
        Returns:
            目标变量Series (0=主队胜, 1=平, 2=客队胜)
        """
        self.logger.info("创建目标变量")
        
        targets = []
        for match in matches_with_results:
            if 'final_score' in match:
                home_goals, away_goals = map(int, match['final_score'].split(':'))
                if home_goals > away_goals:
                    targets.append(0)  # 主队胜
                elif home_goals == away_goals:
                    targets.append(1)  # 平局
                else:
                    targets.append(2)  # 客队胜
        
        return pd.Series(targets)
    
    def normalize_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """特征归一化"""
        self.logger.info("特征归一化")
        
        from sklearn.preprocessing import StandardScaler
        
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        scaler = StandardScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        
        return df

feature_engineer = FeatureEngineer()
