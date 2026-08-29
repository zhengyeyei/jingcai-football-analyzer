"""凯利公式投注策略"""
import math
from typing import Dict
from src.utils.logger import logger

class KellyCriterion:
    """凯利公式 - 优化投注额计算"""
    
    def __init__(self, bankroll: float = 10000):
        """
        Args:
            bankroll: 资金量
        """
        self.bankroll = bankroll
        self.logger = logger
    
    def calculate_optimal_bet(self, prob_win: float, odds: float, kelly_fraction: float = 0.25) -> float:
        """计算最优投注额
        
        Kelly公式: f* = (bp - q) / b
        其中：
        - f* = 積持的资金比例
        - b = 赔率 - 1
        - p = 胜率
        - q = 输率 (1 - p)
        
        Args:
            prob_win: 胜率 (0-1)
            odds: 赔率
            kelly_fraction: Kelly系数 (0-1，越小越保守)
        
        Returns:
            投注额
        """
        # 验证输入
        if prob_win <= 0 or prob_win >= 1:
            self.logger.warning(f"需要有效的胜率 (0-1)，接收: {prob_win}")
            return 0
        
        if odds <= 1:
            self.logger.warning(f"需要有效的赔率 (>1)，接收: {odds}")
            return 0
        
        # 计算Kelly比例
        b = odds - 1
        p = prob_win
        q = 1 - p
        
        kelly_fraction_value = (b * p - q) / b
        
        # 使用分数Kelly
        kelly_fraction_value = kelly_fraction_value * kelly_fraction
        
        # 不允许负值
        if kelly_fraction_value < 0:
            self.logger.info(f"赔率{odds}不优化，跳过投注")
            return 0
        
        # 计算投注额
        bet_size = self.bankroll * kelly_fraction_value
        
        self.logger.info(f"推荐投注: {bet_size:.2f} (胜率{p:.2%}, 赔率{odds}, Kelly系数{kelly_fraction})")
        
        return bet_size
    
    def calculate_win_probability_from_odds(self, odds: float) -> float:
        """从赔率测算输赢概率"""
        return 1 / odds
    
    def calculate_expected_value(self, prob_win: float, odds: float, bet_size: float) -> float:
        """计算期望收益
        
        EV = (p * winnings) - ((1-p) * loss)
        """
        prob_loss = 1 - prob_win
        winnings = bet_size * odds
        loss = bet_size
        
        ev = (prob_win * winnings) - (prob_loss * loss)
        return ev

kelly_criterion = KellyCriterion()
