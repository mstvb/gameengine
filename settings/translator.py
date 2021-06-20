import json


class Translator:
    def __init__(self):
        self.file = None
        self.json = None


    def setLanguage(self, language: str):
        self.file = open(language + ".json")
        self.json = json.loads(self.file.read())


    def getLine(self, key):
        if not self.json:
            return
        else:
            return self.json[key]