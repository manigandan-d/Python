import random
import hangman_stages
import word_list

lives = 6
game_over = False

word = random.choice(word_list.words)

length = len(word)

display = []

for i in range(length):
    display += "_"

print(display)

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()

    for i in range(length):
        if word[i] == guessed_letter:
            display[i] = guessed_letter

    print(display)

    if guessed_letter not in word:
        lives -= 1

        if lives == 0:
            game_over = True
            print("You lose!")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(hangman_stages.stages[lives])

