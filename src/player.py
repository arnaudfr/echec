from src.chessPiece import ChessPiece

class Player:

    def __init__ (self,id):
        if (id < 0):
            raise ValueError()
        else:
            self._id = id
        pass
	self._pieces = []
