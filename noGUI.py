import nltk
import random

nltk.download("words")

def word_list():
    from nltk.corpus import words
    return words.words()

def checkLetter(letter, word):
    return letter in word

def requestLetterCap():

    return int(input("Please enter the number of letters you'd like to cap your word at. If you don't want a cap : enter -1"))

def chooseWord(lettercap,word_list):
    if lettercap == -1:
        return random.choice(word_list)
    while len(word) != lettercap:
        word = random.choice(word_list)
    return word

def updateGuess(letter,word,guessedSoFar):
    gsf = list(guessedSoFar)
    for i in range(len(word)):
        if word[i] == letter:
            gsf[i] = letter
    return ''.join(gsf)


def main():
    wl = word_list()
    cont = True
    while cont:
        lettercap = requestLetterCap()
        word = chooseWord(lettercap,wl)
        guessedSoFar = '_' * len(word)
        chances = 6

        print("Welcome to Hangman! You have to guess the word. You have 6 chances left")
        
        while chances > 0 and '_' in guessedSoFar:
            print(guessedSoFar)
            print(f"You have {chances} chances left.")
            chosenLetter = input("Please enter a letter")[0]

        if(checkLetter(checkLetter, word)):
            print("That letter is in the word")
            guessedSoFar = updateGuess(chosenLetter,word, guessedSoFar)
            if(word == guessedSoFar): 
                print ("You have guessed correctly! The word was: ", word)
        else:
            print("That letter is not in the word")
            chances -=1
        if chances == 0:    
            print("You have run out of chances. The word was " + word)
        
        cont = input("Do you want to play again? (yes/no) :").lower() == "yes"

    
main()