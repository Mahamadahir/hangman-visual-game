import nltk
import random

# Ensure the words corpus is downloaded
nltk.download("words", quiet=True)

def word_list():
    from nltk.corpus import words
    return words.words()

def check_letter(letter, word):
    return letter in word

def request_letter_cap():
    return int(input("Please enter the number of letters you'd like to cap your word at. If you don't want a cap, enter -1: "))

def choose_word(letter_cap, word_list):
    if letter_cap == -1:
        return random.choice(word_list)
    else:
        filtered_words = [word for word in word_list if len(word) == letter_cap]
        return random.choice(filtered_words) if filtered_words else None

def update_guess(letter, word, guessed_so_far):
    return ''.join(letter if letter == word[i] else guessed_so_far[i] for i in range(len(word)))

def main():
    wl = word_list()
    while True:
        letter_cap = request_letter_cap()
        word = choose_word(letter_cap, wl)
        if not word:
            print("No words found with that specific length.")
            continue

        guessed_so_far = '_' * len(word)
        chances = 6

        print("Welcome to Hangman! Guess the word.")
        
        while chances > 0 and '_' in guessed_so_far:
            print(guessed_so_far)
            print(f"You have {chances} chances left.")
            chosen_letter = input("Please enter a letter: ")[0]

            if check_letter(chosen_letter, word):
                new_guess = update_guess(chosen_letter, word, guessed_so_far)
                if new_guess == guessed_so_far:
                    print("No new letter revealed.")
                else:
                    guessed_so_far = new_guess
                    print("Good guess!")
            else:
                chances -= 1
                print("That letter is not in the word.")

            if word == guessed_so_far:
                print(f"You have guessed correctly! The word was: {word}")
                break

        if chances == 0:
            print(f"You have run out of chances. The word was: {word}")
        
        if input("Do you want to play again? (yes/no): ").lower() != "yes":
            break

if __name__ == "__main__":
    main()
