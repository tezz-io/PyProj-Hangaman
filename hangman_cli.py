# Create a Hangman CLI Application

import sys

class Player:
    def __init__(self, name, noOfGuesses, word):
        self.playerName = name
        self.noOfGuesses = noOfGuesses
        self.word = word
        self.wordLength = len(self.word)

        self.guessList = []
        for i in self.word:
            self.guessList.append('_')

        self.currentWord = ""
        for i in self.guessList:
            self.currentWord += i

        
    def play(self):

        # Win Condition
        
        if self.word == self.currentWord:
            print("Congratulations! You have won!")
            sys.exit()

        # Loss Condition 
        
        elif self.noOfGuesses <= 0:
            print("Unfortunately, you have lost!")
            sys.exit()

        # Play Condition
        
        else:
            print("Guesses Left: " + str(self.noOfGuesses))
            print("Your current guess: " + self.currentWord)
            
            guessedChar = input("Enter your guess: ")[0]
            
            self.guess(guessedChar)

    def guess(self, guessedChar):

        doesExist = False

        for i in range(self.wordLength):
            if self.word[i] == guessedChar:
                self.guessList[i] = guessedChar
                doesExist = True

        self.currentWord = ""
        for i in self.guessList:
            self.currentWord += i

        if not doesExist:
            self.noOfGuesses -= 1

        self.play()


player = Player("Tezz", 7, "noodles")
player.play()