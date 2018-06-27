import os
import platform

HOME = os.getenv("HOME", os.getenv("USERPROFILE"))
MODULE_DIR = os.path.dirname(__file__)
CONF_DIR = os.path.join(HOME, ".config", "cloud-assistant.conf")
OS = platform.uname()[0]


import configparser

class Settings:
    def __init__(self):
        self.config = configparser.ConfigParser()
    
    def __create_default(self):
        self.config['ServerConfig'] = {}
        self.config['ServerConfig']['ServerUrlToDav'] = 'https://www.example.com/nextcloud/remote.php/dav/'
        self.config['ServerConfig']['UserName'] = ''
        self.config['ServerConfig']['UserPassword'] = ''

    def load_from_file(self, filepath):
        if os.path.exists(filepath):
            self.config.read(filepath)
        else:
            self.__create_default()
            self.save_to_file(filepath)

    def save_to_file(self, filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w+') as configfile:
            self.config.write(configfile)
