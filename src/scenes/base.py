"""场景基础.

提供场景抽象基类定义，所有具体场景应继承 BaseScene 类。
实现场景声明周期管理接口和通用模板方法。
"""

import abc

import pygame


class BaseScene(abc.ABC):
    """场景抽象基类.

    实现场景的标准生命周期.
    激活场景 -> 处理事件 -> 更新逻辑 -> 绘制画面 -> (循环) -> 离开场景
    """

    @abc.abstractmethod
    def handle_events(self, events: list[pygame.event.Event]) -> None:
        """处理事件的抽象方法.

        Args:
            events: 当前帧的事件列表.

        Returns:
            None.
        """
        pass

    @abc.abstractmethod
    def update(self) -> None:
        """更新游戏逻辑的抽象方法."""
        pass

    @abc.abstractmethod
    def draw(self) -> None:
        """渲染场景的抽象方法."""
        pass

    @abc.abstractmethod
    def on_enter(self) -> None:
        """激活场景时调用的抽象方法."""
        pass

    @abc.abstractmethod
    def on_exit(self) -> None:
        """离开场景时调用的抽象方法."""
        pass
