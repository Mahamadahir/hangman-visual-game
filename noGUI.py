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
    cont = True
    chances = 6
    while cont:
        word = chooseWord(requestLetterCap(),word_list())
        guessedSoFar = _ *len(word)
        print("Welcome to Hangman! You have to guess the word. You have 6 chances left")
        chosenLetter = char(input("Please enter a letter"))
        if(checkLetter(checkLetter, word)):
            guessedSoFar = updateGuess(chosenLetter,word, guessedSoFar)
        if(word == guessedSoFar): 
            cont = False
            print ("You have guessed correctly")
        if(chances == 6):
            cont = False
            print("You have run out of chances. The word was " + word)


    main()
    print("Hello wrld")