from src.constant import *

class ChessPiece:

	def __init__(self,pattern,jump):
		self.jump = jump
		if len(pattern) != 2:
			 raise ValueError('badPattern')
		if pattern[0] <= 0 or pattern[1] <= 0:
			 raise ValueError('negativePattern')
		self.pattern = pattern