"""HTTP请求助手"""
import requests
from typing import Dict, Any, Optional
from src.utils.logger import logger
from config.settings import config

class HTTPHelper:
    """HTTP请求工具类"""
    
    @staticmethod
    def get(url: str, params: Optional[Dict] = None, headers: Optional[Dict] = None) -> Optional[Dict[str, Any]]:
        """发送GET请求"""
        try:
            response = requests.get(
                url,
                params=params,
                headers=headers,
                timeout=config.CRAWL_TIMEOUT
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"GET请求失败: {url}, 错误: {str(e)}")
            return None
    
    @staticmethod
    def post(url: str, data: Optional[Dict] = None, json: Optional[Dict] = None, 
             headers: Optional[Dict] = None) -> Optional[Dict[str, Any]]:
        """发送POST请求"""
        try:
            response = requests.post(
                url,
                data=data,
                json=json,
                headers=headers,
                timeout=config.CRAWL_TIMEOUT
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.error(f"POST请求失败: {url}, 错误: {str(e)}")
            return None

http_helper = HTTPHelper()
