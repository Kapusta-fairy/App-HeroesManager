import os

from config import Config


class GameFiles:

    def __init__(self):
        self.game_path = None
        self.directory = None
        self.conf_path = Config().conf_path

    def get_enabled_list(self) -> list:
        return os.listdir(f'{self.game_path}\\{self.directory}')

    def get_disabled_list(self) -> list:
        return os.listdir(f'{self.conf_path}\\{self.directory}')

    def enable(self, item_name):
        return os.replace(
            f'{self.conf_path}\\{self.directory}\\{item_name}',
            f'{self.game_path}\\{self.directory}\\{item_name}'
        )

    def disable(self, item_name):
        return os.replace(
            f'{self.game_path}\\{self.directory}\\{item_name}',
            f'{self.conf_path}\\{self.directory}\\{item_name}'
        )


class Mods(GameFiles):

    def __init__(self):
        super().__init__()
        self.directory = r'UserMODs'


class Maps(GameFiles):

    def __init__(self):
        super().__init__()
        self.directory = r'Maps'
