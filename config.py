import os
from configparser import ConfigParser


def save_config(dirlist, conf_path):
    if not os.path.exists(conf_path):
        os.makedirs(conf_path)

    ini_path = f'{conf_path}/config.ini'

    if not os.path.exists(ini_path):
        with open(ini_path, 'a') as write_f:
            write_f.write(f'[settings]\npath = {dirlist}')


def get_config(conf_path):
    config = ConfigParser()
    config.read(f'{conf_path}/config.ini')

    return config
