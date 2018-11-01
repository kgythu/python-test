"""
Public
Itt minden publikus. Ez az alapértelmezett.
"""

class Cup0:
	def __init__(self):
		self.color = None
		self.content = None

	def fill(self, beverage):
		self.content = beverage

	def empty(self):
		self.content = None

redCup = Cup0()
redCup.color = "red"
redCup.content = "tea"
redCup.empty()
redCup.fill("coffee")

print(redCup.content)

print("----------------------------------------------------")

"""
Protected
Ezt csak az osztály és leszármazott osztályai látják.
Kívülről nem lehet hozzányúlni.
A Python-ban ez csak virtuálisan, konvencionálisan van így.
Az _ jelentése: ne nyúlj hozzám!
"""

class Cup1:
	def __init__(self):
		self.color = None
		self._content = None # protected variable

	def fill(self, beverage):
		self._content = beverage

	def empty(self):
		self._content = None

blueCup = Cup1()
blueCup._content = "tea"

print(blueCup._content) # Valójában nincs rejtve

print("----------------------------------------------------")

"""
Private
Senki nem férhet hozzá kívülről.
Name mangling! __ kezdetű név => _<className><memberName>
Az __ karaktersor kell a név elejére.
"""

class Cup2:
	def __init__(self, color):
		self._color = color    # protected variable
		self.__content = None  # private variable

	def fill(self, beverage):
		self.__content = beverage

	def empty(self):
		self.__content = None

greenCup = Cup2("green")
greenCup._Cup__content = "tea" # Valójában ez sincs rejtve, csak így kell hivatkozni rá

print(greenCup._Cup__content)

print("----------------------------------------------------")
