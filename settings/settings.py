import json


class Settings:
    def __init__(self):
        self.file = open('settings.json', 'w')
        self.file.write('{}')
        self.file = open('settings.json')
        self.json = json.loads(self.file.read())


    def setValue(self, key, value):
        self.json[key] = value


    def getValue(self, key):
        return self.json[key]


    def saveSettings(self):
        self.file = open('settings.json', 'w')
        self.file.write(json.dumps(self.json))