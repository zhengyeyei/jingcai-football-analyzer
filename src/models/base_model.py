"""基础模型类"""
import pickle
from abc import ABC, abstractmethod
from typing import Any
from src.utils.logger import logger

class BaseModel(ABC):
    """基础模型类"""
    
    def __init__(self, name: str):
        self.name = name
        self.logger = logger
        self.model = None
        self.is_trained = False
    
    @abstractmethod
    def train(self, X_train: Any, y_train: Any) -> None:
        """训练模型"""
        pass
    
    @abstractmethod
    def predict(self, X_test: Any) -> Any:
        """预测"""
        pass
    
    def save_model(self, path: str) -> None:
        """保存模型"""
        if self.model is None:
            self.logger.warning("模型未初始化")
            return
        
        try:
            with open(path, 'wb') as f:
                pickle.dump(self.model, f)
            self.logger.info(f"模型已保存: {path}")
        except Exception as e:
            self.logger.error(f"保存模型失败: {str(e)}")
    
    def load_model(self, path: str) -> None:
        """加载模型"""
        try:
            with open(path, 'rb') as f:
                self.model = pickle.load(f)
            self.is_trained = True
            self.logger.info(f"模型已加载: {path}")
        except Exception as e:
            self.logger.error(f"加载模型失败: {str(e)}")

__all__ = ['BaseModel']
