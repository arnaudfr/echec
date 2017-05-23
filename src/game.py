from src.constant import *
from src.player import Player

class Game:

    # Function to set new grid based on size
    def setGrid(self,size):
        if size > MINGRID and size < MAXGRID:
            self._grid = [[0 for x in range(size)] for y in range(size)]
            return self._grid
        else:
            return 0

    # Return the current grid
    def getGrid(self):
        if self._grid is None:
            return 0
        else:
            return self._grid

    def createPlayer(self):
        self._players[len(self._players)] = Player(len(self._players))
        return self._players[len(self._players)]

    def getPlayer(self,i):
        return self._players[i]