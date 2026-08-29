"""运行爬虫脚本"""
import sys
import time
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.crawler.match_crawler import match_crawler
from src.crawler.odds_crawler import odds_crawler
from src.crawler.team_crawler import team_crawler
from src.processor.data_cleaner import data_cleaner
from src.processor.data_validator import data_validator
from src.utils.logger import logger
from config.settings import config
import json

def main():
    """运行爬虫程序"""
    try:
        logger.info("="*50)
        logger.info("竞彩足球数据爬虫开始运行")
        logger.info("="*50)
        
        # 1. 爬取比赛数据
        logger.info("\n[1/4] 爬取比赛数据...")
        matches = match_crawler.fetch_upcoming_matches(days_ahead=5)
        
        # 2. 验证比赛数据
        logger.info("\n[2/4] 验证比赛数据...")
        valid, errors = data_validator.validate_matches(matches)
        if not valid:
            logger.warning(f"验证错误: {errors}")
        
        # 3. 爬取赔率数据
        logger.info("\n[3/4] 爬取赔率数据...")
        odds_data = odds_crawler.fetch_odds_for_matches(matches)
        
        # 4. 验证赔率数据
        logger.info("\n[4/4] 验证赔率数据...")
        valid, errors = data_validator.validate_odds(odds_data)
        if not valid:
            logger.warning(f"验证错误: {errors}")
        
        # 保存结果
        logger.info("\n成功爬取数据汇总:")
        logger.info(f"  - 比赛数: {len(matches)}场")
        logger.info(f"  - 赔率数: {len(odds_data)}条")
        
        # 打印第一场比赛详情
        if matches and odds_data:
            logger.info("\n第一场比赛確认信息:")
            logger.info(f"  比赛: {matches[0]['home_team']} vs {matches[0]['away_team']}")
            logger.info(f"  比赛时間: {matches[0]['start_time']}")
            logger.info(f"  赔率: 胜{odds_data[0]['odds_sources']['european']['win']} 平{odds_data[0]['odds_sources']['european']['draw']} 负{odds_data[0]['odds_sources']['european']['loss']}")
        
        logger.info("\n爬虫完成！")
        logger.info("="*50)
        return 0
        
    except Exception as e:
        logger.error(f"爬虫过程中出错: {str(e)}", exc_info=True)
        return 1

if __name__ == '__main__':
    sys.exit(main())
