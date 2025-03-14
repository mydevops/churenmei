"""事件.

使用示例:
1. 触发场景切换事件：
>>> event_data = {"scene": "game_over"}
>>> pygame.event.post(pygame.event.Event(GameEvent.SWITCH_TO_GAME_OVER, event_data))

2. 监听处理事件：
>>> for event in pygame.event.get():
...     if event.type == GameEvent.SWITCH_TO_GAME_OVER:
...         # dosomething...
"""

from enum import IntEnum

import pygame


class GameEvent(IntEnum):
    """事件类."""

    # 切换开始游戏场景
    SWITCH_TO_START_GAME = pygame.event.custom_type()
    # 切换游戏场景
    SWITCH_TO_GAME = pygame.event.custom_type()
    # 切换游戏结束场景
    SWITCH_TO_GAME_OVER = pygame.event.custom_type()
