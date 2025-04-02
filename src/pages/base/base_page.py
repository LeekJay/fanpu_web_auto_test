"""
页面对象模式的基类，实现通用的页面操作方法
"""

import os
import time
from contextlib import contextmanager
from typing import Optional, Union

from playwright.sync_api import expect, Page, Frame, Locator
from utils.logger import logger
from config.config import SCREENSHOT_PATH, BASE_URL
from pages.base.base_config import WaitConfig, ElementState, LoadState


class BasePage:
    """页面对象基类，实现通用的页面操作方法"""

    def __init__(self, page: Page):
        """
        初始化基础页面
        :param page: playwright页面对象
        """
        self.page = page
        self.base_url = BASE_URL
        self.current_frame: Optional[Frame] = None
        self._ensure_screenshot_dir()

    def _ensure_screenshot_dir(self):
        """确保截图目录存在"""
        if not os.path.exists(SCREENSHOT_PATH):
            os.makedirs(SCREENSHOT_PATH)

    @contextmanager
    def frame_context(
        self, frame_selector: str, timeout: int = WaitConfig.DEFAULT_TIMEOUT
    ):
        """
        iframe上下文管理器
        :param frame_selector: iframe选择器
        :param timeout: 超时时间(毫秒)
        """
        try:
            self.enter_frame(frame_selector, timeout)
            yield
        finally:
            self.exit_frame()

    def get_context(self) -> Union[Page, Frame]:
        """
        获取当前操作的上下文（iframe或主文档）
        :return: 当前操作的上下文
        """
        return self.current_frame if self.current_frame else self.page

    def _get_element(
        self, selector: str, timeout: int = WaitConfig.DEFAULT_TIMEOUT
    ) -> Locator:
        """
        获取元素定位器
        :param selector: 元素选择器
        :param timeout: 超时时间(毫秒)
        :return: 元素定位器
        """
        context = self.get_context()
        context.wait_for_selector(selector, timeout=timeout)
        return context.locator(selector)

    # 页面导航相关方法
    def navigate(self, url: Optional[str] = None):
        """
        导航到指定页面
        :param url: 目标URL，默认为None，使用base_url
        """
        target_url = url if url else self.base_url
        logger.info(f"导航到: {target_url}")
        self.page.goto(target_url)

    def reload_page(self):
        """刷新页面"""
        logger.info("刷新页面")
        self.page.reload()

    def go_back(self):
        """返回上一页"""
        logger.info("返回上一页")
        self.page.go_back()

    def go_forward(self):
        """前进到下一页"""
        logger.info("前进到下一页")
        self.page.go_forward()

    # 页面状态相关方法
    def stabilize_page(self, timeout: int = WaitConfig.STABILIZE_TIMEOUT):
        """
        稳定页面，防止画面偏移
        :param timeout: 等待时间(毫秒)
        """
        logger.info("稳定页面位置")
        self.page.evaluate("window.scrollTo(0, 0)")
        self.page.wait_for_timeout(timeout)

    def wait_for_navigation(self, timeout: int = WaitConfig.NAVIGATION_TIMEOUT):
        """
        等待页面导航完成
        :param timeout: 超时时间(毫秒)
        """
        logger.info("等待页面导航完成")
        self.page.wait_for_load_state(LoadState.NETWORKIDLE, timeout=timeout)

    def wait_for_iframe_ready(self):
        """等待iframe加载完成"""
        self.page.wait_for_function("""
            () => {
                const iframe = document.querySelector('iframe');
                return iframe && iframe.contentDocument.readyState === 'complete';
            }
        """)

    # iframe 相关方法
    def enter_frame(
        self, frame_selector: str, timeout: int = WaitConfig.DEFAULT_TIMEOUT
    ) -> Frame:
        """
        进入iframe
        :param frame_selector: iframe的选择器
        :param timeout: 超时时间(毫秒)
        :return: iframe对象
        """
        logger.info(f"进入iframe: {frame_selector}")
        frame = self.page.wait_for_selector(frame_selector, timeout=timeout)
        self.current_frame = frame.content_frame()

        if not self.current_frame:
            raise Exception(f"无法获取 iframe: {frame_selector}")

        return self.current_frame

    def exit_frame(self):
        """退出iframe，返回主文档"""
        logger.info("退出iframe，返回主文档")
        self.current_frame = None
        return self.page

    # 元素操作方法
    def click(self, selector: str, timeout: int = WaitConfig.DEFAULT_TIMEOUT):
        """
        点击元素
        :param selector: 元素选择器
        :param timeout: 超时时间(毫秒)
        """
        logger.info(f"点击元素: {selector}")
        self.stabilize_page()
        self._get_element(selector, timeout).click()

    def fill(self, selector: str, text: str, timeout: int = WaitConfig.DEFAULT_TIMEOUT):
        """
        在输入框中填入文本
        :param selector: 元素选择器
        :param text: 要填入的文本
        :param timeout: 超时时间(毫秒)
        """
        logger.info(f"在 {selector} 中填入: {text}")
        self.stabilize_page()
        self._get_element(selector, timeout).fill(text)

    def select_option(
        self,
        selector: str,
        value: Optional[str] = None,
        timeout: int = WaitConfig.DEFAULT_TIMEOUT,
    ):
        """
        选择下拉选项（支持非标准下拉框）
        :param selector: 元素选择器
        :param value: 选项的value值
        :param timeout: 超时时间(毫秒)
        """
        option_text = value
        logger.info(f"在 {selector} 中选择选项: {option_text}")

        # 先等待输入框可见
        self.wait_for_selector(selector, timeout)

        # 先填入文本
        self.fill(selector, option_text)

        # 构建下拉选项的选择器
        dropdown_selector = "li"

        try:
            # 首先尝试精确匹配
            option_selector = f"{dropdown_selector} >> text='{option_text}'"
            logger.info(f"尝试精确匹配选项: {option_text}")
            option = self.get_context().locator(option_selector).first
            option.wait_for(timeout=timeout)
            option.click()
        except Exception:
            # 如果精确匹配失败，尝试模糊匹配
            logger.info(f"精确匹配失败，尝试模糊匹配: {option_text}")
            options = self.get_context().locator(dropdown_selector).all()
            found = False
            for option in options:
                if option_text in option.text_content():
                    option.click()
                    found = True
                    break

            if not found:
                raise Exception(f"未找到包含文本 '{option_text}' 的选项")

    def get_text(self, selector: str, timeout: int = WaitConfig.DEFAULT_TIMEOUT) -> str:
        """
        获取元素文本
        :param selector: 元素选择器
        :param timeout: 超时时间(毫秒)
        :return: 元素文本
        """
        logger.info(f"获取元素 {selector} 的文本")
        element = self._get_element(selector, timeout)
        return (
            element.input_value() if element.is_editable() else element.text_content()
        )

    def get_input_value(
        self, selector: str, timeout: int = WaitConfig.DEFAULT_TIMEOUT
    ) -> str:
        """
        获取输入框的值
        :param selector: 元素选择器
        :param timeout: 超时时间(毫秒)
        :return: 输入框的值
        """
        logger.info(f"获取输入框 {selector} 的值")
        return self._get_element(selector, timeout).input_value()

    # 元素状态检查方法
    def is_visible(
        self, selector: str, timeout: int = WaitConfig.DEFAULT_TIMEOUT
    ) -> bool:
        """
        检查元素是否可见
        :param selector: 元素选择器
        :param timeout: 超时时间(毫秒)
        :return: 元素是否可见
        """
        try:
            expect(self._get_element(selector)).to_be_visible(timeout=timeout)
            return True
        except Exception as e:
            logger.error(f"元素 {selector} 不可见: {e}")
            return False

    def is_value_equal(
        self, selector: str, value: str, timeout: int = WaitConfig.DEFAULT_TIMEOUT
    ) -> bool:
        """
        检查元素的值是否等于给定值
        :param selector: 元素选择器
        :param value: 期望的值
        :param timeout: 超时时间(毫秒)
        :return: 是否相等
        """
        try:
            expect(self._get_element(selector)).to_have_value(value, timeout=timeout)
            return True
        except Exception as e:
            logger.error(f"元素 {selector} 的值不等于 {value}: {e}")
            return False

    # 截图方法
    def take_screenshot(self, name: str = "screenshot") -> str:
        """
        截取屏幕截图
        :param name: 截图名称
        :return: 截图路径
        """
        timestamp = time.strftime("%Y%m%d%H%M%S")
        file_path = os.path.join(SCREENSHOT_PATH, f"{name}_{timestamp}.png")
        logger.info(f"截图保存至: {file_path}")
        self.page.screenshot(path=file_path)
        return file_path

    # 等待方法
    def wait_for_selector(
        self,
        selector: str,
        timeout: int = WaitConfig.DEFAULT_TIMEOUT,
        state: str = None,
    ):
        """
        等待元素出现
        :param selector: 元素选择器
        :param timeout: 超时时间(毫秒)
        """
        logger.info(f"等待元素出现: {selector}")
        return self.get_context().wait_for_selector(
            selector, timeout=timeout, state=state
        )

    def wait_for_element_state(
        self,
        selector: str,
        state: str = ElementState.VISIBLE,
        timeout: int = WaitConfig.DEFAULT_TIMEOUT,
    ):
        """
        等待元素达到指定状态
        :param selector: 元素选择器
        :param state: 期望的状态
        :param timeout: 超时时间(毫秒)
        """
        logger.info(f"等待元素 {selector} 达到状态: {state}")
        self._get_element(selector).wait_for(state=state, timeout=timeout)
