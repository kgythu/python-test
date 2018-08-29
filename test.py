#!/usr/bin/env python3

sep = '--------------------------------------------------------------------------------'
print("Alma")

x = 8
y = 5
print(x // y)

if 0 < x < y:
	print("barack")
elif 0 < x > y:
	print("citrom")
else:
	print("dinnye")

z = "eper"
print(z[len(z)-1:])
print(z[:len(z)-1])

a, b = 8, 4
print(int(a / b))

c = d = 5
print(c * d)

print()

print(sep)
# str
x = "füge"
print(type(x))
x = 'gesztenye'
print(type(x))
x = """h
á
r
s"""
print(type(x))

print(sep)
# bytearray ! ASCII
x = bytearray(b"fuge")
print(type(x))
x = bytearray(b'gesztenye')
print(type(x))
x = bytearray([119, 105, 107, 105])
print(type(x))

print(sep)
# bytes ! ASCII
x = b"fuge"
print(type(x))
x = b'gesztenye'
print(type(x))
x = bytes([119, 105, 107, 105])
print(type(x))

print(sep)
# list
x = [4.0, 'string', True]
print(type(x))

print(sep)
# tuple
x = (4.0, 'string', True)
print(type(x))

print(sep)
# set
x = {4.0, 'string', True}
print(type(x))

print(sep)
# frozenset
x = frozenset([4.0, 'string', True])
print(type(x))

print(sep)
# dict
x = {'key1': 1.0, 3: False}
print(type(x))

print(sep)
#int
x = -145
print(type(x))
x = 0
print(type(x))
x = 26
print(type(x))

print(sep)
# float
x = 3.1415927
print(type(x))
x = 0.0
print(type(x))
x = 45.0
print(type(x))
x = -78.452
print(type(x))

print(sep)
# complex
x = 3 + 2.7j
print(type(x))

print(sep)
# bool
x = True
print(type(x))
x = False
print(type(x))

print(sep)
# ellipsis
x = ...
print(type(x))

print(sep)
# range
x = range(10)
print(type(x))
# list(x)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = range(1, 11)
print(type(x))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = range(0, 30, 5)
print(type(x))
# [0, 5, 10, 15, 20, 25]
x = range(0, 10, 3)
print(type(x))
# [0, 3, 6, 9]
x = range(0, -10, -1)
print(type(x))
# [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
x = range(0)
print(type(x))
# []
x = range(1, 0)
print(type(x))
# []

print(sep)
x = 3 + 2.7j
print(str(x))
print(type(str(x)))
print(x.real)
print(type(x.real))
print(abs(x))
print(type(abs(x)))

print(sep)
x = [4.0, 'string', True]
print(type(x))
print(x)
x = x[0] + 5
print(type(x))
print(x)
x = [4.0, 'string', True]
x[0] = 5
print(type(x))
print(x)

print(sep)
x = (4.0, 'string', True)
print(type(x))
print(x)
x = x[0] + 5
print(type(x))
print(x)

# x = (4.0, 'string', True)
# x[0] = 5
# TypeError: 'tuple' object does not support item assignment
# x = {4.0, 'string', True}
# x = x[0] + 5
# TypeError: 'set' object does not support indexing
# x = {4.0, 'string', True}
# x[0] = 5
# TypeError: 'set' object does not support item assignment
# x = frozenset([4.0, 'string', True])
# x = x[0] + 5
# TypeError: 'frozenset' object does not support indexing
# x = frozenset([4.0, 'string', True])
# x[0] = 5
# TypeError: 'frozenset' object does not support item assignment

print(sep)
x = {'a': 4.0, 'b': 'string', 'c': True}
print(type(x))
print(x)
# x = x[0] + 5
# KeyError: 0
x = x['a'] + 5
print(type(x))
print(x)
x = {'a': 4.0, 'b': 'string', 'c': True}
x[0] = 5
print(type(x))
print(x)
x = {'a': 4.0, 'b': 'string', 'c': True}
x['a'] = 5
print(type(x))
print(x)
x["a"] = 5
print(type(x))
print(x)

print(sep)
x = "füge"
print(type(x))
print(x)
# x = x[0] + 5
# TypeError: must be str, not int
x = x[0] + str(5)
print(type(x))
print(x)
# x = "füge"
# x[0] = 5
# TypeError: 'str' object does not support item assignment

print(sep)
x = bytearray(b"fuge")
print(type(x))
print(x)
x = x[0] + 5
print(type(x))
print(x)
x = bytearray(b"fuge")
x[0] = 75
print(type(x))
print(x)

print(sep)
x = b"fuge"
print(type(x))
print(x)
x = x[0] + 5
print(type(x))
print(x)
# x = b"fuge"
# x[0] = 75
# TypeError: 'bytes' object does not support item assignment

print(sep)
def switch(x):
	return {
		'a': 'alma',
		'b': 'barack',
		'c': 'citrom'
	}.get(x, 'dinnye') # 'dinnye' is default if x not found

def switchB(x):
	return {
		'a': 'alma',
		'b': 'barack',
		'c': 'citrom'
	}[x]

def switchC(x):
	try:
		return {
			'a': 'alma',
			'b': 'barack',
			'c': 'citrom'
		}[x]
	except(KeyError):
		return 'dinnye' # 'dinnye' is default if x not found

def switchD(x):
	if x == 'a':
		return 'alma'
	elif x == 'b':
		return 'barack'
	elif x == 'c':
		return 'citrom'
	else:
		return 'dinnye'

print(switch('a'))
print(switch('f'))
print(switchB('a'))
# print(switchB('f'))
# KeyError: 'f'
print(switchC('a'))
print(switchC('f'))
print(switchD('a'))
print(switchD('f'))

print(sep)
x = ['liszt', 3, 'tojás', 5, 'cukor']
y = 0
while y < len(x):
	print(str(y) + ': ' + str(x[y]))
	y += 1;
else:
	print('ennyi')

print(sep)
x = ['liszt', 3, 'tojás', 5, 'cukor']
for i in range(0, len(x)):
	print(str(i) + ': ' + str(x[i]))
else:
	print('ennyi')

print(sep)
x = ['liszt', 3, 'tojás', 5, 'cukor']
print(type(x))
print(x)
x = 3 * x[:3] + ['margarin']
print(type(x))
print(x)


