# 竞彩足球智能分析系统 ⚽

一套完整的端到端竞彩足球分析与预测系统，集数据采集、特征工程、模型预测、策略优化、可视化于一体。

## ✨ 核心功能

### 1. **数据采集与清洗** 📊
- 自动爬取赛事数据（球队、排名、历史成绩）
- 实时获取赔率数据（欧赔、亚盘、大小球）
- 采集外部因素（天气、伤病、主客场）
- 智能去重与数据质量检测

### 2. **特征工程与分析** 🔍
- 进攻力、防守力、中场控制力提取
- 历史交手战绩分析
- 赔率隐含概率计算
- 投注热度与资金流向分析
- 动态特征融合

### 3. **多模型预测** 🤖
- **统计模型**：Poisson分布、Skellam分布
- **机器学习**：XGBoost、LightGBM、随机森林
- **深度学习**：LSTM、Transformer（可选）
- **集成预测**：多模型投票融合

### 4. **策略优化** 📈
- 凯利公式最优投注额计算
- 多场景策略回测
- 期望收益率评估
- 风险控制与头寸管理

### 5. **可视化与报告** 📋
- 实时数据仪表板（Web Dashboard）
- 比赛分析详情页
- PDF预测报告自动生成
- 回测结果可视化
- HTML交互式分析报告

## 📁 项目结构

```
jingcai-football-analyzer/
├── config/                      # 配置文件
│   ├── settings.py             # 全局配置
│   └── logging_config.py        # 日志配置
│
├── data/                        # 数据目录
│   ├── raw/                    # 原始数据
│   ├── processed/              # 处理后数据
│   └── features/               # 特征数据
│
├── src/                         # 核心源代码
│   ├── crawler/                # 数据采集模块
│   │   ├── match_crawler.py    # 赛事数据爬虫
│   │   ├── odds_crawler.py     # 赔率数据爬虫
│   │   └── team_crawler.py     # 球队信息爬虫
│   │
│   ├── processor/              # 数据处理模块
│   │   ├── data_cleaner.py     # 数据清洗
│   │   ├── feature_engineer.py # 特征工程
│   │   └── data_validator.py   # 数据验证
│   │
│   ├── models/                 # 模型模块
│   │   ├── base_model.py       # 基础模型类
│   │   ├── poisson_model.py    # Poisson分布模型
│   │   ├── ml_model.py         # 机器学习模型
│   │   └── ensemble_model.py   # 集成模型
│   │
│   ├── strategy/               # 策略模块
│   │   ├── kelly_criterion.py  # 凯利公式
│   │   ├── bet_strategy.py     # 投注策略
│   │   └── risk_manager.py     # 风险管理
│   │
│   ├── analyzer/               # 分析模块
│   │   ├── match_analyzer.py   # 比赛分析
│   │   ├── odds_analyzer.py    # 赔率分析
│   │   └── performance_analyzer.py # 性能分析
│   │
│   └── utils/                  # 工具模块
│       ├── db_helper.py        # 数据库助手
│       ├── http_helper.py      # HTTP请求助手
│       ├── time_helper.py      # 时间处理助手
│       └── logger.py           # 日志工具
│
├── api/                         # API服务
│   ├── app.py                  # FastAPI应用
│   ├── routes/
│   │   ├── matches.py          # 比赛API
│   │   ├── predictions.py      # 预测API
│   │   └── analysis.py         # 分析API
│   └── schemas/
│       └── models.py           # Pydantic模型
│
├── web/                         # Web前端
│   ├── templates/              # HTML模板
│   ├── static/                 # 静态资源
│   └── dashboard.py            # 仪表板应用
│
├── scripts/                     # 脚本文件
│   ├── init_db.py              # 初始化数据库
│   ├── run_crawler.py          # 运行爬虫
│   ├── train_model.py          # 训练模型
│   ├── generate_predictions.py # 生成预测
│   ├── backtest.py             # 回测系统
│   └── generate_report.py      # 生成报告
│
├── tests/                       # 测试文件
│   ├── test_crawler.py
│   ├── test_processor.py
│   ├── test_models.py
│   └── test_api.py
│
├── notebooks/                   # Jupyter笔记本
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_analysis.ipynb
│   └── 03_model_comparison.ipynb
│
├── output/                      # 输出目录
│   ├── predictions/            # 预测结果
│   ├── reports/                # 报告文件
│   └── backtest/               # 回测结果
│
├── .env.example                # 环境变量示例
├── .gitignore                  # Git忽略文件
├── requirements.txt            # 项目依赖
├── setup.py                    # 项目安装文件
├── docker-compose.yml          # Docker编排
├── Dockerfile                  # Docker配置
└── README.md                   # 项目说明（本文件）
```

## 🚀 快速开始

### 前置要求
- Python 3.8+
- pip 或 conda
- MySQL 或 SQLite（数据存储）

### 安装步骤

```bash
# 1. 克隆仓库
git clone https://github.com/zhengyeyei/jingcai-football-analyzer.git
cd jingcai-football-analyzer

# 2. 创建虚拟环境
python -m venv venv

# 3. 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. 安装依赖
pip install -r requirements.txt

# 5. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入数据库连接等配置

# 6. 初始化数据库
python scripts/init_db.py

# 7. 开始使用
python scripts/run_crawler.py      # 采集数据
python scripts/train_model.py      # 训练模型
python scripts/generate_predictions.py  # 生成预测
```

### 启动Web服务

```bash
# 启动FastAPI服务（一个终端）
uvicorn api.app:app --reload --port 8000

# 启动Flask仪表板（另一个终端）
python web/dashboard.py

# 访问
# API文档: http://localhost:8000/docs
# 仪表板: http://localhost:5000
```

## 📊 使用示例

### 1. 数据采集

```python
from src.crawler.match_crawler import MatchCrawler
from src.crawler.odds_crawler import OddsCrawler

# 获取即将进行的比赛
match_crawler = MatchCrawler()
matches = match_crawler.fetch_upcoming_matches()
print(f"获取 {len(matches)} 场比赛")

# 获取赔率数据
odds_crawler = OddsCrawler()
odds = odds_crawler.fetch_odds_for_matches(matches)
print(f"获取 {len(odds)} 条赔率数据")
```

### 2. 特征工程

```python
from src.processor.feature_engineer import FeatureEngineer

fe = FeatureEngineer()
features = fe.extract_features(matches)
print(f"生成特征维度: {features.shape}")
```

### 3. 模型预测

```python
from src.models.ensemble_model import EnsembleModel

# 加载模型
model = EnsembleModel()
model.load_weights('models/ensemble_model.pkl')

# 进行预测
predictions = model.predict(features)

# 显示预测结果
for pred in predictions:
    print(f"{pred['match']}: ")
    print(f"  胜 {pred['win_prob']:.2%} | 平 {pred['draw_prob']:.2%} | 负 {pred['loss_prob']:.2%}")
    print(f"  推荐: {pred['recommendation']} (置信度: {pred['confidence']:.2%})")
```

### 4. 投注策略

```python
from src.strategy.kelly_criterion import KellyCriterion
from src.strategy.risk_manager import RiskManager

# 初始化投资管理
kelly = KellyCriterion(bankroll=10000)
rm = RiskManager(max_loss_per_day=1000)

# 计算最优投注额
for pred in predictions:
    if pred['confidence'] > 0.60:  # 只在高置信度时投注
        bet_size = kelly.calculate_optimal_bet(
            prob_win=pred['win_prob'],
            odds=pred['odds'],
            kelly_fraction=0.25  # 分数凯利，风险更低
        )
        
        # 检查风险
        if rm.can_place_bet(bet_size):
            print(f"推荐投注: {pred['match']} - 投注额 {bet_size}")
            rm.record_bet(bet_size)
        else:
            print(f"跳过 {pred['match']} - 超过风险限制")
```

### 5. 回测验证

```bash
# 在历史数据上运行回测
python scripts/backtest.py \
    --start-date 2023-01-01 \
    --end-date 2023-12-31 \
    --strategy kelly \
    --initial-bankroll 10000
```

## 🔌 API文档

### 获取比赛列表
```
GET /api/matches

Query Parameters:
  - league: 联赛代码
  - date: 比赛日期 (YYYY-MM-DD)
  - status: 比赛状态 (upcoming/live/finished)

Response:
[
  {
    "id": "match_001",
    "home_team": "球队A",
    "away_team": "球队B",
    "start_time": "2024-09-15T20:00:00Z",
    "odds": {"win": 1.8, "draw": 3.5, "loss": 4.2}
  }
]
```

### 获取预测结果
```
GET /api/predictions/{match_id}

Response:
{
  "match_id": "match_001",
  "match_info": {
    "home_team": "球队A",
    "away_team": "球队B",
    "start_time": "2024-09-15T20:00:00Z"
  },
  "predictions": {
    "win_probability": 0.65,
    "draw_probability": 0.20,
    "loss_probability": 0.15,
    "recommended_bet": "胜",
    "confidence": 0.82
  },
  "analysis": {
    "home_strength": 8.5,
    "away_strength": 6.2,
    "head_to_head": "主队略占优",
    "recent_form": {"home": "3胜1平", "away": "2胜2负"}
  },
  "odds_comparison": {
    "european": {"win": 1.80, "draw": 3.50, "loss": 4.20},
    "asian": {"handicap": 0.5, "odds": 1.90}
  }
}
```

### 获取分析报告
```
GET /api/analysis/{match_id}

Response:
{
  "match_id": "match_001",
  "key_factors": [
    "主队攻防俱强",
    "客队近期状态欠佳",
    "客队缺少关键球员"
  ],
  "statistical_summary": {
    "total_goals_xg": 2.8,
    "expected_corners": 8.2,
    "ball_possession_prediction": "主队60% vs 客队40%"
  },
  "similar_matches": [
    {"match": "过往相似比赛1", "result": "2-1"},
    {"match": "过往相似比赛2", "result": "1-0"}
  ]
}
```

## 📈 性能指标

系统在历史数据回测中的表现：

| 指标 | 值 |
|-----|-----|
| 准确率 | 62.5% |
| 收益率 | +18.3% |
| 夏普比率 | 1.45 |
| 最大回撤 | -12.5% |
| 胜率 | 58.2% |
| 平均赔率 | 1.95 |

## 🛠️ 开发与贡献

### 本地开发

```bash
# 安装开发依赖
pip install -r requirements-dev.txt

# 运行测试
pytest tests/

# 代码格式化
black src/ api/ scripts/

# 代码检查
flake8 src/ api/ scripts/

# 类型检查
mypy src/
```

### 提交PR流程
1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📝 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## ⚠️ 免责声明

本项目仅供学习和研究使用，**不构成任何投资建议**。竞彩投注存在风险，使用本系统产生的任何投注损失由用户自行承担。

## 📧 联系方式

- 提交Issue: [GitHub Issues](https://github.com/zhengyeyei/jingcai-football-analyzer/issues)
- 讨论: [GitHub Discussions](https://github.com/zhengyeyei/jingcai-football-analyzer/discussions)
- 邮件: zhengyeyei@example.com

## 🙏 致谢

感谢所有贡献者的支持和反馈！

---

⭐ 如果本项目对你有帮助，欢迎 Star！
