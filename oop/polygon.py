"""
Polygon osztály
Pontok alapján kezel egy sokszöget.
"""
import math

class Poligon:
	# Konstruktor
	def __init__(self, vertices):
		self.__sides = 0
		self.setVertices(vertices)

	# Metódusok
	def measureLine(self, a, b):
		if(type(a).__name__ != "Point"):
			raise ValueError("A szakasz csúcspontja nem megfelelő!")
		if(type(b).__name__ != "Point"):
			raise ValueError("A szakasz csúcspontja nem megfelelő!")
		return math.sqrt((a.getX() - b.getX()) ** 2 + (a.getY() - b.getY()) ** 2)

	def measureAbsolutAngle(self, a, v):
		# a: pont a száron
		# v: csúcspont
		#
		# Pontok ellenőrzése
		if(type(a).__name__ != "Point"):
			raise ValueError("A száron lévő pont nem megfelelő!")
		if(type(v).__name__ != "Point"):
			raise ValueError("A szög csúcspontja nem megfelelő!")
		# A szár abszolút szöge a koordináta rendszerben
		if(a.getX() == v.getX()):
			if(a.getY() == v.getY()):
				raise ValueError("A száron megadott pont a szög csúcspontján található.")
			elif(a.getY() > v.getY()):
				a_angle = math.pi / 2
			else:
				a_angle = math.pi * 3 / 2
		elif(a.getY() == v.getY()):
			if(a.getX() > v.getX()):
				a_angle = 0
			else:
				a_angle = math.pi
		elif(a.getY() > v.getY()):
			if(a.getX() > v.getX()):
				a_angle = math.atan((a.getY() - v.getY()) / (a.getX() - v.getX()))
			else:
				a_angle = math.pi - math.atan((a.getY() - v.getY()) / (v.getX() - a.getX()))
		else:
			if(a.getX() > v.getX()):
				a_angle = math.pi + math.atan((v.getY() - a.getY()) / (a.getX() - v.getX()))
			else:
				a_angle = math.pi * 2 - math.atan((v.getY() - a.getY()) / (v.getX() - a.getX()))
		return a_angle

	def measureAngle(self, a, v, b):
		# a, b: pontok a szárakon
		# v: csúcspont
		#
		# Első szár abszolút szöge a koordináta rendszerben
		a_angle = self.measureAbsolutAngle(a, v)
		# Második szár abszolút szöge a koordináta rendszerben
		b_angle = self.measureAbsolutAngle(b, v)
		# Két szár hegyesebbik szöge
		if(a_angle > b_angle):
			h_angle = a_angle - b_angle
		elif(a_angle < b_angle):
			h_angle = b_angle - a_angle
		else:
			raise ValueError("A két szár nem alkot szöget!")
		# Két szár tompábbik szöge
		t_angle = math.pi * 2 - h_angle
		return (h_angle, t_angle, a_angle, b_angle)

	# Szetterek
	def setVertices(self, vertices):
		if(type(vertices) is tuple):
			for vertex in vertices:
				if(type(vertex).__name__ != "Point"):
					raise ValueError("A csúcspont nem megfelelő!")
			if(len(vertices) < 3):
				raise ValueError("Egy sokszögnek minimum három csúcsa van!")
			elif((self.__sides != 0) and (self.__sides != len(vertices))):
				raise ValueError("Ennek a típusú sokszögnek kötelezően " + str(self.__sides) + " csúcsa van!")
		else:
			raise ValueError("Nem megfelelő csúcspontlista!")
		self.__vertices = vertices
		self.setPerimeter()
		self.setArea()

	def setPerimeter(self):
		self.__perimeter = 0
		for i in range(len(self.__vertices)):
			if(i == 0):
				j = len(self.__vertices) - 1
			else:
				j = i - 1
			self.__perimeter += self.measureLine(self.__vertices[i], self.__vertices[j])

	def setArea(self):
		self.__area = 1
		if(len(self.__vertices) == 3):
			self.setAreaTriangle()
		else:
			raise Exception("Nincs képletünk a sokszög területének kiszámításához.")

	def setAreaTriangle(self):
		# Képlet: a × b × sin gamma / 2
		self.__area *= self.measureLine(self.__vertices[0], self.__vertices[1])
		self.__area *= self.measureLine(self.__vertices[1], self.__vertices[2])
		self.__area *= math.sin(self.measureAngle(self.__vertices[0], self.__vertices[1], self.__vertices[2])[0])
		self.__area /= 2

	# Getterek
	def getVertices(self):
		return self.__vertices

	def getPerimeter(self):
		return round(self.__perimeter * 100) / 100

	def getArea(self):
		return round(self.__area * 100) / 100
