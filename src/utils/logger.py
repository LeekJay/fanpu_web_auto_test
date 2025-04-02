"""
日志工具，用于记录测试过程中的日志信息
"""

import logging
import os
from datetime import datetime


class Logger:
    """日志工具类"""

    def __init__(self, logger_name="web_auto_test"):
        """
        初始化日志器
        :param logger_name: 日志器名称
        """
        # 创建日志目录
        log_dir = os.path.join(
            os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            ),
            "reports",
            "logs",
        )
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 创建日志器
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.INFO)

        # 避免重复添加处理器
        if not self.logger.handlers:
            # 控制台处理器
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # 文件处理器
            log_file = os.path.join(
                log_dir, f"{datetime.now().strftime('%Y%m%d%H%M%S')}.log"
            )
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setLevel(logging.INFO)

            # 设置日志格式
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            console_handler.setFormatter(formatter)
            file_handler.setFormatter(formatter)

            # 添加处理器
            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def info(self, message):
        """记录信息日志"""
        self.logger.info(message)

    def warning(self, message):
        """记录警告日志"""
        self.logger.warning(message)

    def error(self, message):
        """记录错误日志"""
        self.logger.error(message)

    def debug(self, message):
        """记录调试日志"""
        self.logger.debug(message)

    def critical(self, message):
        """记录严重错误日志"""
        self.logger.critical(message)


# 创建全局日志器实例
logger = Logger().logger
