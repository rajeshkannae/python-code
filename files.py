with open('learning_python.txt') as file_object:
	#contents = file_object.read()
	lines = file_object.readlines()

#print(contents)

for line in lines:
	print(line)

with open('writefile.txt', 'w') as file_object:
	file_object.write('hi this is rajesh\n')
	file_object.write('how are you guys\n')

with open('writefile.txt', 'a') as file_object:
	file_object.write('adding append text')


