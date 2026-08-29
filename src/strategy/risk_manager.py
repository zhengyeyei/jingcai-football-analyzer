"""风险管理"""
from typing import Dict, List
from src.utils.logger import logger

class RiskManager:
    """资金风险管理器"""
    
    def __init__(self, initial_bankroll: float = 10000, max_loss_per_day: float = 1000):
        self.initial_bankroll = initial_bankroll
        self.current_bankroll = initial_bankroll
        self.max_loss_per_day = max_loss_per_day
        self.daily_loss = 0
        self.max_single_bet_ratio = 0.05  # 单次投注不超资金5%
        self.logger = logger
    
    def can_place_bet(self, bet_amount: float) -> bool:
        """检查是否可以下注
        
        Args:
            bet_amount: 投注额
        
        Returns:
            是否可以下注
        """
        # 检查单次投注不超过最大比例
        if bet_amount > self.current_bankroll * self.max_single_bet_ratio:
            self.logger.warning(f"投注额{bet_amount}超过了资金的{self.max_single_bet_ratio:.1%}")
            return False
        
        # 检查是否超过了最大损失限制
        if self.daily_loss + bet_amount > self.max_loss_per_day:
            self.logger.warning(f"当日损失已超过限制: {self.daily_loss + bet_amount} > {self.max_loss_per_day}")
            return False
        
        # 检查网执是否正常
        if bet_amount > self.current_bankroll:
            self.logger.error("投注额超过了当前资金")
            return False
        
        return True
    
    def record_bet(self, bet_amount: float, result: str = None) -> None:
        """记录投注
        
        Args:
            bet_amount: 投注额
            result: 投注结果 ('win'或'loss')
        """
        if result is None:
            # 仅记录投注，暂不计算损益
            self.current_bankroll -= bet_amount
            self.daily_loss += bet_amount
        elif result == 'win':
            # 胜利
            self.current_bankroll += bet_amount
            self.logger.info(f"投注胜利: +{bet_amount}, 当前资金: {self.current_bankroll}")
        elif result == 'loss':
            # 输了
            self.daily_loss += bet_amount
            self.logger.warning(f"投注输了: -{bet_amount}, 当前资金: {self.current_bankroll}")
    
    def reset_daily_loss(self) -> None:
        """重置当日损失计数"""
        self.daily_loss = 0
        self.logger.info("当日损失计数已重置")
    
    def get_status(self) -> Dict:
        """获取风险管理状态"""
        return {
            'initial_bankroll': self.initial_bankroll,
            'current_bankroll': self.current_bankroll,
            'profit_loss': self.current_bankroll - self.initial_bankroll,
            'daily_loss': self.daily_loss,
            'max_loss_per_day': self.max_loss_per_day,
            'remaining_daily_limit': self.max_loss_per_day - self.daily_loss
        }

risk_manager = RiskManager()
