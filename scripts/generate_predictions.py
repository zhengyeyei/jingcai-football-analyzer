"""生成预测脚本"""
import sys
import os
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.crawler.match_crawler import match_crawler
from src.processor.feature_engineer import feature_engineer
from src.models.ensemble_model import ensemble_model
from src.strategy.kelly_criterion import kelly_criterion
from src.strategy.risk_manager import risk_manager
from src.utils.logger import logger
import json

def main():
    """生成预测"""
    try:
        logger.info("="*50)
        logger.info("预测生成开始")
        logger.info("="*50)
        
        # 1. 载入模型
        logger.info("\n[1/4] 加载模型...")
        model_path = 'models/ensemble_model.pkl'
        if not os.path.exists(model_path):
            logger.warning(f"模型文件不存在: {model_path}")
            logger.info("正使用未训练的模型进行预测...")
        else:
            ensemble_model.load_model(model_path)
        
        # 2. 获取比赛数据
        logger.info("\n[2/4] 载入比赛数据...")
        matches = match_crawler.fetch_upcoming_matches(days_ahead=5)
        logger.info(f"获取{len(matches)}场比赛")
        
        # 3. 提取特征
        logger.info("\n[3/4] 特征提取...")
        features = feature_engineer.extract_features(matches)
        logger.info(f"特征新成: {features.shape}")
        
        # 4. 进行预测
        logger.info("\n[4/4] 执行预测...")
        predictions = ensemble_model.predict(features)
        
        # 打印预测结果
        logger.info("\n预测结果汇总:")
        logger.info("-" * 80)
        
        for pred in predictions:
            match_info = f"{pred['home_team']} vs {pred['away_team']}"
            logger.info(f"\n比赛: {match_info}")
            logger.info(f"  胜率: {pred['win_prob']:.2%} | 平率: {pred['draw_prob']:.2%} | 负率: {pred['loss_prob']:.2%}")
            logger.info(f"  推荐: {pred['recommendation']} (置信度: {pred['confidence']:.2%})")
            
            # 计算投注额
            if pred['confidence'] > 0.60:
                bet_amount = kelly_criterion.calculate_optimal_bet(
                    prob_win=pred['win_prob'] if pred['recommendation'] == '胜' else pred['draw_prob'] if pred['recommendation'] == '平' else pred['loss_prob'],
                    odds=pred['odds'].get('win' if pred['recommendation'] == '胜' else 'draw' if pred['recommendation'] == '平' else 'loss', 1.8),
                    kelly_fraction=0.25
                )
                logger.info(f"  推荐投注: {bet_amount:.2f}元")
        
        logger.info("\n" + "-" * 80)
        logger.info(f"预测完成！总计{len(predictions)}场比赛")
        logger.info("="*50)
        
        # 保存预测结果
        output_dir = 'output/predictions'
        os.makedirs(output_dir, exist_ok=True)
        
        output_file = f"{output_dir}/predictions_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(predictions, f, ensure_ascii=False, indent=2)
        logger.info(f"\n预测结果已保存: {output_file}")
        
        return 0
        
    except Exception as e:
        logger.error(f"预测过程中出错: {str(e)}", exc_info=True)
        return 1

if __name__ == '__main__':
    import pandas as pd
    sys.exit(main())
