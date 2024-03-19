import random
lst = ['r','p','s']
result = {
	('r','r'):'tie',
	('r','p'):'lost',
	('s','p'):'won',
	('s','r'):'lost',
	('r','s'):'won',
	('p','r'):'won',
	('p','s'):'lost',
	('p','p'):'tie',
	('s','s'):'tie'
}


print("--- Rock Paper Scissors Game ---")
round_no = int(input("How many rounds would you like to play?"))

your_point=0
computer_point=0

for i in range(round_no):
	choice = input("Rock, paper or scissors [r/p/s]?")
	computer_choice = random.choice(lst)
	print("You: " + choice + " | Computer: " + computer_choice)
	print("You " + result[(choice,computer_choice)] + " this round!")
	if result[(choice,computer_choice)] == 'won':
		your_point +=1
	elif result[(choice,computer_choice)] == 'lost':
		computer_point += 1

print("[Game summary] Your points: " + str(your_point) + " | Computer points: " + str(computer_point))
if your_point>computer_point:
	print("You won.")
elif your_point<computer_point:
	print("Computer won.")
else:
	print("It was a tie")




