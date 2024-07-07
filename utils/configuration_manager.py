import json

class ConfigurationManager:
    def __init__(self, config_file='data/config.json'):
        with open(config_file, 'r') as file:
            self.config = json.load(file)

    def get_config(self, key):
        return self.config.get(key, None)