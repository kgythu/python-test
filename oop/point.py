"""
Pont osztály
Egy kétdimenziós koordináta-rendszerben helyez el egy pontot.
"""
class Point:
	# Konstruktor
	def __init__(self, x, y):
		self.setX(x)
		self.setY(y)

	# Szetterek
	def setX(self, x):
		self.__x = x

	def setY(self, y):
		self.__y = y

	# Getterek
	def getX(self):
		return self.__x

	def getY(self):
		return self.__y
