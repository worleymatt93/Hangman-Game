import random
import hangman_art
import hangman_words


print(hangman_art.logo)
lives = 6
print(hangman_art.stages[lives])

chosen_word = random.choice(hangman_words.word_list)

game_word = ["_" for symbol in chosen_word]
print("".join(game_word))

guessed_letters = []
game_over = False
while not game_over:

    guess = input("Guess a letter: ").strip().lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter")
        continue

    if guess in guessed_letters:
        print(f"You already guessed {guess}.  Try again.")
    else:
        guessed_letters.append(guess)

        for i, letter in enumerate(chosen_word):
            if letter == guess:
                game_word[i] = letter

        if guess not in chosen_word:
            lives -= 1
            print(f"Wrong guess. You have {lives} lives left")
            print(hangman_art.stages[lives])
        else:
            print("Good guess!")

    if lives > 0:
        print("".join(game_word))
    else:
        game_over = True
        print("He's dead...")
        print(f"The word was {chosen_word}")

    if "_" not in game_word:
        game_over = True
        print("YOU WON!")
        print(f"The word was {chosen_word}")
