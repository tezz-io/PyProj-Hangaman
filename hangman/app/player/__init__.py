import sys

class Player:
    def __init__(self, name, noOfGuesses, word):
        self.playerName = name
        self.noOfGuesses = noOfGuesses
        self.word = word.upper()
        self.finalWord = ""
        for i in self.word:
            self.finalWord += i + " "
        self.wordLength = len(self.word)

        self.guessList = []
        for i in self.word:
            self.guessList.append('_')

        self.currentWord = ""
        for i in self.guessList:
            self.currentWord += i + " "

        
    def play(self, guessedChar):

        # # Win Condition
        
        # if self.word == self.currentWord:
        #     print("Congratulations! You have won!")
        #     sys.exit()

        # # Loss Condition 
        
        # elif self.noOfGuesses <= 0:
        #     print("Unfortunately, you have lost!")
        #     sys.exit()

        # Play Condition
        
        # else:
            # print("Guesses Left: " + str(self.noOfGuesses))
            # print("Your current guess: " + self.currentWord)
            
        self.guess(guessedChar)

    def guess(self, guessedChar):

        doesExist = False

        for i in range(self.wordLength):
            if self.word[i] == guessedChar:
                self.guessList[i] = guessedChar
                doesExist = True

        self.currentWord = ""
        for i in self.guessList:
            self.currentWord += i + " "

        if not doesExist:
            self.noOfGuesses -= 1


