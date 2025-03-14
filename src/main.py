"""游戏入口."""

import pygame

from scene_manager import SceneManager
from scenes.game_over_scene import GameOverScene
from scenes.game_scene import GameScene
from scenes.start_scene import StartGameScene
from src import config
from src.events import GameEvent


def main() -> None:
    """游戏入口程序."""
    pygame.init()
    pygame.display.set_caption(config.TITLE)
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    scene_manager = SceneManager(StartGameScene(screen))

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            elif event.type == GameEvent.SWITCH_TO_START_GAME:
                scene_manager.switch_to_scene(StartGameScene(screen))
            elif event.type == GameEvent.SWITCH_TO_GAME:
                scene_manager.switch_to_scene(GameScene(screen))
            elif event.type == GameEvent.SWITCH_TO_GAME_OVER:
                scene_manager.switch_to_scene(GameOverScene(screen))

        scene_manager.current_scene.handle_events(events)
        scene_manager.current_scene.update()
        scene_manager.current_scene.draw()

        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
