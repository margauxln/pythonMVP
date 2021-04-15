class View:
    def __init__(self):
        pass
    def displayWordToGuess(self, secretWord, randomWord):
        print ("Bienvenue sur notre pendu")
        print ("Voici le mot a deviner")
        print(randomWord)
        print (secretWord)

    def guessLetter(self):
        print ("Tente une lettre")
        letter = input()
        return letter

    def alreadyTriedLetterView(self):
        print ("Vous avez deja proposé cette lettre")

    def mistakeView(self, mistakes):
        print("eh non dsl, il ne te reste plus que")
        print(str(11 - mistakes) + " tentative(s)")

    def gameOverView(self):
        print("Game Over 💀")  

    def gameWonView(self):
        print("Bravo! Bien joué")