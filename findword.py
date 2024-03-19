word="bit"
count=0
with open("first_file.txt", 'r') as f:
	for line in f:
		words=line.split(" ")
		for i in words:
			if i.isalnum():
				i=i
			if i==word:
				count=count+1

print(count)
