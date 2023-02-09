import random

from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

chosen_word = random.choice(word_list)
print("your word is " + chosen_word)
# guess array
guess_array = []
lives = len(stages) - 1
for i in range(0, len(chosen_word)):
    guess_array.append("_")
print(guess_array)
end_of_game = False
print(stages[lives])
while not end_of_game:
    guess_letter = input("Guess a letter :")
    letter_guessed = False
    for pos in range(0, len(chosen_word)):
        letter = chosen_word[pos]
        if guess_letter == letter:
            guess_array[pos] = letter
            letter_guessed = True
    print(f"{' '.join(guess_array)}")
    if not letter_guessed:
        lives -= 1
        print("Loose a life")
    # Exit clause
    if "_" not in guess_array:
        end_of_game = True
        print("You Win")
    elif lives == 0:
        end_of_game = True
        print("You Loose")
    print(stages[lives])
