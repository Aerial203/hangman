from hangman_art import stages
from hangman_words import word_list
import random

lives = 6
chosen_word = random.choice(word_list)
display = []
game_over = False
guessed_word = []

for word in chosen_word:
    display += "_"

print(f"Psst the word is {chosen_word}")

while not  game_over:
    print(f"{''.join(display)}")
    guess = input("Enter your guess: ").lower()
    if guess in guessed_word:
        print("You have already guessed that alphabet.")
    else:
        for position in range(0, len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if "_" not in display:
            print(f"You have guessed it. Its {chosen_word}")
            print("You Won!")
            game_over = True

        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                print("You loose.")
                print(f"The word is {chosen_word}")
                print("You cannot save the poor man")
                game_over = True

    if guess not in guessed_word:
        guessed_word.append(guess)

    print(stages[lives])
