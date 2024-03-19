

class Car():
	def __init__(self,initial_speed=0):
		self.speed = initial_speed

	def slow_down(self):
		self.speed -= 5


car = Car()
car.slow_down()
car.slow_down()
print(car.speed)

class A:
	x='X'
	def alarm(self):
		print('a' + self.x)

class B(A):
	def alarm(self):
		super().alarm()

class C(B):
	x='y'

C().alarm()

def a():
	hey=5
	def b():
		print(hey)

		return b

x=a()
print(x)

class X:
	Y=1
	def __init__(self):
		self.z=0

print(hasattr(X,'z'))

class Art():
	masterpiece='rajesh'
	def __init__(self):
		self.name='One'

print(Art().__dict__)
print(len(Art().__dict__))


print(__name__)

class Dog:
	def __init__(self, breed='none'):
		self.breed=breed

	def set(self,breed='labrador'):
		self.breed=breed
		return self.breed

puppy=Dog()
friend=puppy
friend.set()
print(puppy.breed)

try:
	raise Exception(0,1,[0,1])
except Exception as e:
	print(len(e.args))

class Server:
	def __init__(self,colour):
		self.colour=colour
		self.name='Rajesh'

myserv=Server('black')
myserv.attr='extra'
print(len(myserv.__dict__))

k=[['*' for i in range(1,3)] for j in range(2)]
print(k)

class A:
	b=1
	def __init__(self):
		self.c=0


print(hasattr(A,'c'))
