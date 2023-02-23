import os

from config import Config


class GameFiles:

    def __init__(self):
        self.game_path = None
        self.directory = None
        self.conf_path = Config().conf_path

    def get_list(self, enabled=True) -> list:
        """Gives the enabled items by default.
        :arg enabled: return enabled items if true or disabled if false
        :return: list of items"""
        if enabled:
            path = self.game_path
        else:
            path = self.conf_path

        return os.listdir(f'{path}{self.directory}')

    def enable(self):
        pass


class Mods(GameFiles):

    def __init__(self):
        super().__init__()
        self.directory = r'\UserMODs'

    def enable(self):
        pass

    def remove(self, mod_name):
        pass


class Maps(GameFiles):

    def __init__(self):
        super().__init__()
        self.directory = r'\Maps'

    def add(self, map_name):
        pass

    def remove(self, map_name):
        pass
