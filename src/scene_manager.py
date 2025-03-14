"""场景管理."""

from src.scenes.base import BaseScene


class SceneManager:
    """场景管理器."""

    def __init__(self, start_scene: BaseScene) -> None:
        """构造器.

        Args:
            start_scene: 初始化场景.
        """
        self.current_scene: BaseScene = start_scene
        self.current_scene.on_enter()

    def switch_to_scene(self, new_scene: BaseScene) -> None:
        """切换场景.

        Args:
            new_scene: 新场景.

        Returns:
            None.
        """
        self.current_scene.on_exit()
        self.current_scene = new_scene
        self.current_scene.on_enter()
