"""开始游戏场景."""

import pygame

from src import config
from src.events import GameEvent
from src.scenes.base import BaseScene


class StartGameScene(BaseScene):
    """开始游戏场景类."""

    def __init__(self, screen: pygame.Surface):
        """构造器."""
        self.screen: pygame.Surface = screen
        self.font: pygame.font.Font = pygame.font.Font(config.FONT_PATH, 30)

    def handle_events(self, events: list[pygame.event.EventType]) -> None:
        """处理事件."""
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.event.post(pygame.event.Event(GameEvent.SWITCH_TO_GAME))

    def update(self) -> None:
        """更新场景逻辑."""
        pass

    def draw(self) -> None:
        """绘制场景内容."""
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.font.render("Start Game Scene", True, (255, 255, 255)), (0, 0))

    def on_enter(self) -> None:
        """激活场景时调用."""
        print("StartGameScene on_enter.")

    def on_exit(self) -> None:
        """离开场景时调用."""
        print("StartGameScene on_exit.")
