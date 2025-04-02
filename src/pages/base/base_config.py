"""
基础页面配置
"""

from dataclasses import dataclass


@dataclass
class WaitConfig:
    """等待配置"""

    DEFAULT_TIMEOUT: int = 10000  # 默认超时时间(毫秒)
    NAVIGATION_TIMEOUT: int = 30000  # 导航超时时间(毫秒)
    STABILIZE_TIMEOUT: int = 1000  # 页面稳定等待时间(毫秒)


@dataclass
class ElementState:
    """元素状态"""

    VISIBLE: str = "visible"
    HIDDEN: str = "hidden"
    ATTACHED: str = "attached"
    DETACHED: str = "detached"


@dataclass
class LoadState:
    """页面加载状态"""

    LOAD: str = "load"
    DOMCONTENTLOADED: str = "domcontentloaded"
    NETWORKIDLE: str = "networkidle"
