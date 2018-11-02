from point import Point
from polygon import Poligon
from triangle import Triangle

a = Point(-3, 3)
b = Point(4, 0)
c = Point(0, 0)

a = Point(-4, 2)
b = Point(4, -6)
c = Point(0, -2)

a = Point(0, 3)
b = Point(4, 0)
c = Point(0, 0)

try:
	triangle = Triangle((a, b, c))
	print("Kerület: " + str(triangle.getPerimeter()))
	print("Terület: " + str(triangle.getArea()))
except ValueError as err:
	print("Hiba: " + err.args[0])
except Exception as err:
	print("Hiba: " + err.args[0])
