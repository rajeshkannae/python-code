class TestClass:
	__x = "hello"

	def __init__(self, first):
		self.first = first

	def __str__(self):
		return TestClass.__x + " " + self.first


tc = TestClass("Rajesh")
print(tc)

