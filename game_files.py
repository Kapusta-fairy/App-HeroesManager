import os

from PyQt5.QtCore import Qt

from config import Config


class GameFiles:

    def __init__(self):
        config = Config()
        self.game_path = config.get().get('settings', 'path')
        self.conf_path = config.conf_path
        self.directory = None

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

        if not os.path.exists(f'{self.conf_path}\\{self.directory}'):
            os.makedirs(f'{self.conf_path}\\{self.directory}')


class Maps(GameFiles):

    def __init__(self):
        super().__init__()
        self.directory = r'Maps'

        if not os.path.exists(f'{self.conf_path}\\{self.directory}'):
            os.makedirs(f'{self.conf_path}\\{self.directory}')
