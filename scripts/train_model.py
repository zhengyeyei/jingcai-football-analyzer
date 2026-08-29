"""训练模型脚本"""
import sys
import os
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.crawler.match_crawler import match_crawler
from src.crawler.team_crawler import team_crawler
from src.processor.feature_engineer import feature_engineer
from src.processor.data_cleaner import data_cleaner
from src.models.ensemble_model import ensemble_model
from src.utils.logger import logger
import pandas as pd

def main():
    """训练模型"""
    try:
        logger.info("="*50)
        logger.info("模型训练开始")
        logger.info("="*50)
        
        # 1. 获取比赛数据（作为训练数据）
        logger.info("\n[1/4] 载入训练数据...")
        matches = match_crawler.fetch_upcoming_matches(days_ahead=10)
        
        # 模拟已完成的比赛结果
        finished_matches = match_crawler.fetch_finished_matches()
        logger.info(f"加载{len(finished_matches)}条已完成比赛数据")
        
        # 2. 特征工程
        logger.info("\n[2/4] 特征提取...")
        X_train = feature_engineer.extract_features(finished_matches)
        
        # 模拟目标变量 (0=胜, 1=平, 2=负)
        y_train = pd.Series([0] * (len(X_train)//2) + [1] * (len(X_train)//4) + [2] * (len(X_train) - len(X_train)//2 - len(X_train)//4))
        logger.info(f"特征新成: {X_train.shape}")
        logger.info(f"目标数据: {len(y_train)}条")
        
        # 3. 训练模型
        logger.info("\n[3/4] 训练集成模型...")
        ensemble_model.train(X_train, y_train)
        
        # 4. 保存模型
        logger.info("\n[4/4] 保存模型...")
        model_path = 'models/ensemble_model.pkl'
        os.makedirs(os.path.dirname(model_path) or '.', exist_ok=True)
        ensemble_model.save_model(model_path)
        
        logger.info("\n模型训练完成！")
        logger.info("="*50)
        return 0
        
    except Exception as e:
        logger.error(f"训练过程中出错: {str(e)}", exc_info=True)
        return 1

if __name__ == '__main__':
    sys.exit(main())
