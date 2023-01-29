import random

paper = '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)⠀⠀⠀⠀⠀⠀⠀
'''
rock = '''
⠀⠀⠀⠀_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''
game_images = [rock, paper, scissors]
user_chose = int(input("What do you choose? 0 for rock, 1 for paper, 2 for scissors \n"))
print(game_images[user_chose])
if 2 < user_chose < 0:
    print("You have typed an invalid input")
else:
    computer_chose = random.randint(0, 2)
    print("computer chose:")
    print(game_images[computer_chose])

    if user_chose == computer_chose:
        print("TIE")
    elif user_chose == 0:
        if computer_chose == 1:
            print("Computer wins")
        elif computer_chose == 2:
            print("You win")
    elif user_chose == 1:
        if computer_chose == 2:
            print("Computer wins")
        elif computer_chose == 0:
            print("You win")
    elif user_chose == 2:
        if computer_chose == 0:
            print("Computer wins")
        elif computer_chose == 1:
            print("You win")
