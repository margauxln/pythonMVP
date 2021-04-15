from unidecode import unidecode
from random import choice
import numpy as np

class Pendu:
    def __init__(self, userName):
        self.word = ""
        self.userName = userName
        self.mistakes = 0 #ne peut aller que jusqu'a 11
        self.triedLetters = []
        self.empty = []

    def setWord(self,word):
        self.word = word

    def alreadyTriedLetter(self,letter):
        self.triedLetters.append(letter)

    def getEmpty(self, word):
        for i in range(len(word)):
            self.empty.append("_")
        return self.empty

    def updateEmpty(self,letter):
        arrayWord = list(self.word)
        for k in range(len(arrayWord)):
            if arrayWord[k] == letter:
                self.empty[k]=letter
        return self.empty

    def updateMistakes(self):
        self.mistakes +=1

    def setUserName():
        pass
