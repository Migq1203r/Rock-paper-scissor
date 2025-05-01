import random
scissor = '''
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
rock = ''' 
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

rps = ['0','1','2']
computer = random.choice(rps)
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
people = input('>>> ')

if people == '0':
    print(rock)
elif people == '1':
    print(paper)
elif people == '2':
    print(scissor)
else:
    print("Option isn't founded in system!")

print("\nComputer Choose: \n")

if computer == '0':
    print(rock)
elif computer == '1':
    print(paper)
else:
    print(scissor)

print("\n\n")
if people == '0' and computer == '0':
    print("It's a Draw!")
elif people == '1' and computer == '1':
    print("It's a Draw!")
elif people == '2' and computer == '2':
    print("It's a Draw!")

if people == '0' and computer == "1":
    print("You Lose ❌")
elif people == '1' and computer == '2':
    print("You Lose ❌")
elif people == '2' and computer == '0':
    print("You Lose ❌")
elif people == '2' and computer == '1':
    print("You Win 🏆")
elif people == '0' and computer == '2':
    print("You Win 🏆")
elif people == '1' and computer == '0':
    print("You Win 🏆")
else:
    print("Option isn't founded in system!")


