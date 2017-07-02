from src.constant import *

class ChessPiece:

	def __init_(self,pattern,jump):
		self.jump = jump
		if len(pattern) != 2:
			return None
		if pattern[0] < 0 or pattern[1] < 0 :
			return None
		self.pattern = pattern