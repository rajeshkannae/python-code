import uuid

class Tasks:
	choice = 0
	nolist = 0
	def __init__(self, choice):
		self.choice=choice

	def run_task(self):
		if self.choice == 1:
			self.task1()
		elif self.choice == 2:
			self.task2()
		elif self.choice == 3:
			self.task3()
		elif self.choice == 4:
			return

	def task1(self):
		print("[YOUR TASKS]")
		self.nolist = 0
		try:
			stream = open("tasks.txt","r")
			lines = stream.readlines()
			
			if len(lines) > 0 :
				for line in lines:
					print(' | '.join(line.strip('\n').split(';')))
				self.nolist = 1
			else:
				print("Empty list")
				
			stream.close()
		except:
			print("Empty list")

	def task2(self):
		print("[ADD TASK]")
		task_question = input("What is the task? ")
		task_deadline = input("What is the deadline? ")
		try:
			stream = open("tasks.txt","a")
			stream.write(str(uuid.uuid4()) + ";" + task_question + ";" + task_deadline)
			stream.write("\n")
			stream.close()
		except:
			print("Error in writing file")

	def task3(self):
		print("[COMPLETE TASK]\n")
		self.task1()

		if self.nolist == 0:
			print("No tasks to complete")
		elif self.nolist == 1:
			list_choice = input("Enter id to complete: ")
			with open("tasks.txt", "r") as fp:
				lines = fp.readlines()

			with open("tasks.txt", "w") as fp:
				for line in lines:
					if line.strip("\n").find(list_choice) == -1:
						fp.write(line)




in_choice = 0

while in_choice != 4:
	print("== TODO LIST ==")
	print("[1] show tasks")
	print("[2] add task")
	print("[3] complete task")
	print("[4] exit")

	in_choice = int(input("Your Choice: "))
	task_obj = Tasks(int(in_choice))
	task_obj.run_task()


