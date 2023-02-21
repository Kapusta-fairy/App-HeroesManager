import os
from configparser import ConfigParser


class ManagerConfig:

    def __init__(self):
        self.conf_path = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\' \
                    f'KapustaInc\\HeroesManager'
        self.conf_file = r'\config.ini'
        self.ini_path = f'{self.conf_path}{self.conf_file}'

    def save(self, dirlist):
        if not os.path.exists(self.conf_path):
            os.makedirs(self.conf_path)

        if not os.path.exists(self.ini_path):
            with open(self.ini_path, 'a') as write_f:
                write_f.write(f'[settings]\npath = {dirlist}')

    def get(self):
        config = ConfigParser()
        config.read(self.ini_path)

        return config
