from penduModel import Pendu
from view import View
from unidecode import unidecode
from random import choice

class Controller:
    pendu = Pendu("toto")
    view = View()

    print(pendu.userName)
    
    def __init__(self):
        pass

    def chooseWord(self):
        f = open('mots.txt', 'r')
        contenu = f.readlines()
        randomWord = unidecode(choice(contenu)).upper().replace('\n','')
        self.pendu.setWord(randomWord)
        hiddenWord = self.pendu.getEmpty(randomWord)
        self.view.displayWordToGuess(hiddenWord,randomWord)

    def getUserInput(self):
        letter = self.view.guessLetter().upper()
        if letter in self.pendu.triedLetters:
            self.view.alreadyTriedLetterView()
        else:
            self.pendu.alreadyTriedLetter(letter)
            if(letter in self.pendu.word):
                print(self.pendu.updateEmpty(letter))
            else:
                self.pendu.updateMistakes()
                self.view.mistakeView(self.pendu.mistakes)

    def gameOver(self):
        self.view.gameOverView()

    def gameWon(self):
        self.view.gameWonView()

def initGame():
    game = Controller()
    game.chooseWord()
    while (game.pendu.mistakes<11 and game.pendu.word != "".join(map(str,game.pendu.empty))):
        game.getUserInput()
    if (game.pendu.mistakes==11):
        game.gameOver()
    if (game.pendu.word == "".join(map(str,game.pendu.empty))):
        game.gameWon()

if __name__ == "__main__":
    initGame()