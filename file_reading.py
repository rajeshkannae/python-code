with open ('learning_python.txt') as file_object:
	contents = file_object.read()


print(contents * 3)

print("******")

with open ('learning_python.txt') as file_object:
	for line in file_object:
		print(line.rstrip())

print("******")

with open ('learning_python.txt') as file_object:
	contents_line = file_object.readlines()

for line in contents_line:
	print(line.rstrip())

print("******")

contents = contents.replace('Python','C')

print(contents)

with open('file_write.txt','w') as file_object:
	file_object.write('I love programming.')

with open('file_write.txt','a') as file_object:
	file_object.write('\nI love creating new games')


try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by Zero")


# try:
# 	a=int(input("Enter number 1"))
# 	b=int(input("Enter number 2"))
# 	print(a+b)
# except ValueError:
# 	print("Input should be numeric")

try:
	with open("cats.txt") as file_object:
		content = file_object.read()
	print(content)

	with open("dogs.txt") as file_object:
		content = file_object.read()
	print(content)

except FileNotFoundError:
	pass
else:
	print("")


