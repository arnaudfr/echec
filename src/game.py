from src.constant import *

class Game:

    def setGrid(self,size):
        if size > MINGRID:
            self._grid = [[0 for x in range(size)] for y in range(size)]
            return 1
        else:
            return 0

    def getGrid(self):
        if self._grid is None:
            return 0
        else:
            return self._grid