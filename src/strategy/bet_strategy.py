"""投注策略"""
from typing import Dict, List
from src.utils.logger import logger

class BetStrategy:
    """投注策略管理器"""
    
    def __init__(self):
        self.logger = logger
    
    def flat_betting(self, predictions: List[Dict], bet_amount: float, min_confidence: float = 0.60) -> List[Dict]:
        """固定资金投注策略
        
        不论预测的置信度，股林公式中模型的投注额都是固定的。
        """
        self.logger.info(f"使用固定资金投注策略: {bet_amount}元/次")
        
        bets = []
        for pred in predictions:
            if pred.get('confidence', 0) >= min_confidence:
                bet = {
                    'match_id': pred['match_id'],
                    'home_team': pred['home_team'],
                    'away_team': pred['away_team'],
                    'recommendation': pred['recommendation'],
                    'confidence': pred['confidence'],
                    'bet_amount': bet_amount,
                    'strategy': 'flat_betting'
                }
                bets.append(bet)
        
        return bets
    
    def confidence_based_betting(self, predictions: List[Dict], base_amount: float, 
                                  min_confidence: float = 0.55) -> List[Dict]:
        """不优化资金-置信度会很开开地增涨很少的投注额。
        
        稀稀需要一个高置信度的预测来使资金翻一倍。
        """
        self.logger.info(f"使用置信度根据投注策略: 基数{base_amount}元")
        
        bets = []
        for pred in predictions:
            if pred.get('confidence', 0) >= min_confidence:
                # 置信度资金买卖比率
                confidence = pred.get('confidence', 0.5)
                # Map confidence to multiplier: 0.55 -> 1x, 1.0 -> 2x
                multiplier = 1 + (confidence - min_confidence) / (1 - min_confidence)
                bet_amount = base_amount * multiplier
                
                bet = {
                    'match_id': pred['match_id'],
                    'home_team': pred['home_team'],
                    'away_team': pred['away_team'],
                    'recommendation': pred['recommendation'],
                    'confidence': pred['confidence'],
                    'bet_amount': bet_amount,
                    'multiplier': multiplier,
                    'strategy': 'confidence_based_betting'
                }
                bets.append(bet)
        
        return bets
    
    def value_betting(self, predictions: List[Dict], base_amount: float) -> List[Dict]:
        """价值投注 - 只在疑集概率比赔率暗示概率高时投注
        
        平均赔率 = 1 / 暗示概率
        比较预测概率不同
        """
        self.logger.info(f"使用价值投注策略: 基数{base_amount}元")
        
        bets = []
        for pred in predictions:
            odds = pred.get('odds', {})
            
            # 根据推荐类型抓住相关赔率
            if pred['recommendation'] == '胜':
                current_odds = odds.get('win', 1.8)
            elif pred['recommendation'] == '平':
                current_odds = odds.get('draw', 3.5)
            else:  # 负
                current_odds = odds.get('loss', 4.2)
            
            # 暗示概率
            implied_prob = 1 / current_odds
            
            # 比较预测概率与暗示概率
            if pred['recommendation'] == '胜':
                predicted_prob = pred['win_prob']
            elif pred['recommendation'] == '平':
                predicted_prob = pred['draw_prob']
            else:
                predicted_prob = pred['loss_prob']
            
            # 只在有优势时投注（预测概率 > 暗示概率）
            if predicted_prob > implied_prob:
                value = (predicted_prob - implied_prob) / implied_prob
                bet_amount = base_amount * (1 + value)  # 根据优势大小预算
                
                bet = {
                    'match_id': pred['match_id'],
                    'home_team': pred['home_team'],
                    'away_team': pred['away_team'],
                    'recommendation': pred['recommendation'],
                    'predicted_prob': predicted_prob,
                    'implied_prob': implied_prob,
                    'value': value,
                    'bet_amount': bet_amount,
                    'strategy': 'value_betting'
                }
                bets.append(bet)
        
        return bets

bet_strategy = BetStrategy()
