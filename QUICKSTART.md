"""安装成功后的下一步指南

这个脚本帮助你快速开始使用模型预测系统
"""

import subprocess
import sys
from pathlib import Path
from src.utils.logger import logger

print("\n" + "="*70)
print("🏼 竞彩足球智能分析系统 - 快速开始指南")
print("="*70)

print("""
✅ 你的环境已成功配置！

下一步你可以使用以下命令来运行系统的各个模块:

[📄 初始化数据库]
  python scripts/init_db.py
  
  作用: 初始化数据库表结构
  执行次数: 第一次扩展性时（正常情况下一次执行）

[📄 运行爬虫]
  python scripts/run_crawler.py
  
  作用: 爬取比赛数据、赔率数据、球队信息
  执行次数: 每天（推荐）
  提示: 第一次运行帮无法接入真实数据源的情况下，正在使用模拟数据

[📄 训练模型]
  python scripts/train_model.py
  
  作用: 使用历史数据训练预测模型
  执行次数: 处理足够数据后一次 (30+ 比赛)
  提示: 上线前必需这一步！

[📄 生成预测]
  python scripts/generate_predictions.py
  
  作用: 对下一场比赛进行预测
  执行次数: 需要的时候
  提示: 结果及推荐投注额需测会显示

[📄 运行API服务]
  uvicorn api.app:app --reload --port 8000
  
  作用: 启动FastAPI应用，提供RESTful API
  访问: http://localhost:8000/docs
  提示: 可以用Postman或curl测试API端点

[📄 运行仪表板]
  python web/dashboard.py
  
  作用: 启动Web仪表板（需要Flask）
  访问: http://localhost:5000
  提示: 待实现

" ")

print("\n[🚀 快速开始三步走]")
print("""
1。初始化数据库（可选）:
   python scripts/init_db.py

2、运行爬虫获取数据:
   python scripts/run_crawler.py

3、训练模型（第一次）:
   python scripts/train_model.py

4、生成预测：
   python scripts/generate_predictions.py

""")

print("\n[🧠 常见问题]")
print("""
Q: 第一次运行时执行阶段是什么顺序？
A: init_db -> run_crawler -> train_model -> generate_predictions

Q: 为什么会提示数据源不可用？
A: 场噪数据源需要你与帅你插接，一个私有API。
   一旦你插接API，只需修改config中URL配置。

Q: 预测结果的模拟数据为什么总是是一样的？
A: 模拟数据故意推设化了一亟投注场景。
   待接入真实数据后会自动更改。

""")

print("[🎧 是否要执行创建船脚本?]")
print("""
\u5229用我们提供的脚本，你可以一个一个回测分析最旦一场比赛的预测结果。

有任何问题，请查看 README.md 或打开issue。
""")

print("\n" + "="*70)
print("🚀 写代码是很有趣的，一鈙就上森了！")
print("="*70 + "\n")
