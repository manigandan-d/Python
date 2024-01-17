import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print('\nWinning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

    if user_choice < 0 or user_choice > 2:
        print("You typed invalid number, you lose!")

    else:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)

        print("Computer chose: ")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You win!")

        elif user_choice == 2 and computer_choice == 0:
            print("You lose!")

        elif user_choice > computer_choice:
            print("You win!")

        elif user_choice < computer_choice:
            print("You lose!")

        elif user_choice == computer_choice:
            print("It's a draw")

    play = input("Do you want to play again? (y/n): ")

    if play.lower() == 'n':
        break

print("\nThanks for playing\n")
