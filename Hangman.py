import random
from hangman_shape import hangman, half_hangman, more_half_hangman, half_less_hangman, hangman_1
from words import english_words

underscore = []
lives = 5
game_over = False
words_list = english_words

chosen_word = random.choice(words_list)

for i in chosen_word:
    underscore += '_'
print(underscore)
while not game_over:
    guessed_letter = input("Guess a Letter: ").lower()
    if guessed_letter not in underscore:
        for i in range(len(chosen_word)):
            new_letter = chosen_word[i]
            if new_letter == guessed_letter:
                underscore[i] = guessed_letter
        print(underscore)

        if guessed_letter not in chosen_word:
            lives -= 1
            print(lives, "Chance Remaining ")
            if lives == 0:
                print("Woo Yar! You have Lose the game! ")
                game_over = True
        if lives == 4:
            print(hangman_1)

        if lives == 3:
            print(half_less_hangman)
        if lives == 2:
            print(more_half_hangman)
        if lives == 1:
            print(half_hangman)
        if lives == 0:
            print(hangman)

        else:
            if '_' not in underscore:
                print("Yay! You Win the game ")
                print(lives, "Chance Where Remaining When you win")
                game_over = True
    else:
        print("You have already type this letter")
