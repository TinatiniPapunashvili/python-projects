# Program: Word Guessing Game (Like Hangman)

import random
def choose_word():
    words = ["Computer Science", "Neuroscience", "Programming", "Python", "Psychology", 
              "Philosophy", "Math", "Random", "Water","CS","Biology"]
    # choice() returns a randomly selected word from words list
    return random.choice(words)

def word_status(word, guessed_letters):
  # Loop through the word one letter at at time, concatenating the letter
  # to the display string if it IS a guess_letter and _ if it is not
    display = ""
    for letter in word:
        if letter in guessed_letters:
           display += letter
        else:
           display += "_"
    return display

def word_guessing_game():
    secret_word = choose_word()
    guessed_letters = []
    attempts = 7

    print("Word Guessing Game")
    print("*********")
    print("Secret Word:", word_status(secret_word, guessed_letters))

    while attempts > 0:
         
        guess = input("Guess A Letter:" ).lower()

        if len(guess) != 1 or not guess.isalpha():
            print("You must enter a single letter.")
            continue 
        if guess in guessed_letters:
            print("you already guessed that letter.")
            continue
        guessed_letters.append(guess)

        # If the guessed letter is NOT in the word to be guessed the player
        # loses an attempt and we output a message informing them of this 
        # and the number of remaining attempts they have left.

        if guess not in secret_word:
            attempts -= 1
            print(f"No letter, '{guess}' occurs in the word.")
            print(f"You have {attempts} attempts remaining.")
        else:
            occurrences = secret_word.count(guess)
            print(f"Letter '{guess}' occurs {occurences} times.")
          
        current_status = word_status(secret_word, guessed_letters)
        print("Secret Word: ", current_status)

        if "_" not in current_status:
            print("Congrats! You guessed the word.")
            break

    # If the player runs out of attempts and there is an _ character in the 
    # status of the word this means the user failed to guess all the letters 
    # before running out of attempts.  In this case we just inform the user 
    # of this and output what the word to be guessed was.
        
    if "_" in current_status:
        print(f"You ran out of attemps! The word was: {secret_word}")

word_guessing_game()