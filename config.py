import os
from configparser import ConfigParser

from data import heroes_paths


class Config:

    def __init__(self):
        self.conf_path = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\' \
                    f'KapustaInc\\HeroesManager'
        self.ini_path = f'{self.conf_path}\\config.ini'

        if not os.path.exists(self.ini_path):
            self.save()

    def save(self, dirlist=None):
        if not os.path.exists(self.conf_path):
            os.makedirs(self.conf_path)

        if dirlist:
            path = dirlist
        else:
            path = self.__heroes_search()
        if not path:
            path = 'Путь не найден, укажите вручную'

        with open(self.ini_path, 'w') as write_f:
            write_f.write(f'[settings]\npath = {path}')

    def get(self):
        config = ConfigParser()
        config.read(self.ini_path)

        return config

    @staticmethod
    def __heroes_search():
        for heroes_path in heroes_paths:
            if os.path.exists(heroes_path):

                return heroes_path
