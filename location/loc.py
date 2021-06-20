class Location2D:
    def __init__(self, x=0, y=0):
        self.loc = [x, y]


    def setLocation(self, x, y):
        self.loc = [x, y]


    def setPosX(self, x):
        self.loc[0] = x


    def setPosY(self, y):
        self.loc[1] = y


    def getLocation(self):
        return self.loc


    def getPosX(self):
        return self.loc[0]


    def getPosY(self):
        return self.loc[1]


class Location3D:
    def __init__(self, x=0, y=0, z=0):
        self.loc = [x, y, z]


    def setLocation(self, x, y, z):
        self.loc = [x, y, z]


    def setPosX(self, x):
        self.loc[0] = x


    def setPosY(self, y):
        self.loc[1] = y


    def setPosZ(self, z):
        self.loc[2] = z


    def getLocation(self):
        return self.loc


    def getPosX(self):
        return self.loc[0]


    def getPosY(self):
        return self.loc[1]


    def getPosZ(self):
        return self.loc[2]