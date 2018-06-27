import os
import platform

HOME = os.getenv("HOME", os.getenv("USERPROFILE"))
MODULE_DIR = os.path.dirname(__file__)
CONF_DIR = os.path.join(HOME, ".config", "cloudassist.conf")
OS = platform.uname()[0]


import configparser

class Settings:
    @property
    def server_url_dav(self):
        return self.config['ServerConfig']['ServerUrlDav']

    @property
    def user_name(self):
        return self.config['ServerConfig']['UserName']

    @property
    def user_password(self):
        return self.config['ServerConfig']['UserPassword']

    @property
    def proxy(self):
        proxy_conf = self.config['ServerConfig']['Proxy']
        if proxy_conf == '':
            return None
        else:
            return proxy_conf

    def __init__(self):
        self.config = configparser.ConfigParser()

    def __create_default(self):
        self.config['ServerConfig'] = {}
        self.config['ServerConfig']['ServerUrlDav'] = 'https://www.example.com/nextcloud/remote.php/dav/'
        self.config['ServerConfig']['UserName'] = ''
        self.config['ServerConfig']['UserPassword'] = ''
        self.config['ServerConfig']['Proxy'] = ''

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
