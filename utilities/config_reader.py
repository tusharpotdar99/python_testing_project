import configparser


config = configparser.ConfigParser()

config.read('config/config.ini')

class ConfigReader:

    @staticmethod
    def get_url():
        return config['DEFAULT']['url']

    @staticmethod
    def get_browser():
        return config['DEFAULT']['browser']

    @staticmethod
    def get_username():
        return config['DEFAULT']['username']

    @staticmethod
    def get_password():
        return config['DEFAULT']['password']

    @staticmethod
    def get_timeout():
        return config['DEFAULT']['timeout']

