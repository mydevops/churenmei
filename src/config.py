"""配置.

使用示例:
>>> from src import config
>>> config.SCREEN_WIDTH
>>> config.SCREEN_HEIGHT
"""

from typing import Final


# 屏幕宽度
SCREEN_WIDTH: Final[int] = 1280
# 屏幕高度
SCREEN_HEIGHT: Final[int] = 720
# 每秒刷新帧数
FPS: Final[int] = 60
# 窗口标题
TITLE: Final[str] = "楚人美"
# 字体路径
FONT_PATH: Final[str] = "../assets/fonts/simkai.ttf"
