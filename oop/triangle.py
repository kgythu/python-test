"""
Triangle osztály
Pontok alapján kezel egy háromszöget.
"""
from polygon import Poligon

class Triangle(Poligon):
	# Konstruktor
	def __init__(self, vertices):
		# Trükközni kell
		self._Poligon__sides = 3
		try:
			self.setVertices(vertices)
		except ValueError as err:
			if(err.args[0] == "A két szár nem alkot szöget!"):
				raise ValueError("A megadott pontok nem alkotnak háromszöget!")
			raise ValueError(err.args)
		except Exception as err:
			raise Exception(err.args)
