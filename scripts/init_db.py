"""初始化数据库脚本"""
import sys
from pathlib import Path

# 添加项目路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.db_helper import db_helper
from src.utils.logger import logger

def main():
    """初始化数据库"""
    try:
        logger.info("开始初始化数据库...")
        db_helper.init_db()
        logger.info("数据库初始化成功！")
    except Exception as e:
        logger.error(f"数据库初始化失败: {str(e)}")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
