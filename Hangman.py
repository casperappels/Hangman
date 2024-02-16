SecretWord = ""
SecretList = []
gallow = (9,8,7,6,5,4,3,2,1,"game over")

def GetSecretWord():    #function below prints the gallow doodle afterwards it request a secret word and returns this.
    
    print( """
        _____________
        |            |
        |            |
        |            0
        |           \|/
        |            |
        |           /|
        |
        |
        |_________""")
    SecretWordFunction = input("Don't let the other look, what will be your secret word? ")
    return SecretWordFunction

SecretWord = GetSecretWord()
for letter in SecretWord:
    SecretList.append(letter)

print(SecretList)
WordLenght = len(SecretWord)

def PrintWordLenght():
    print("the lenght of your secret word is " + str(WordLenght))

def GetGuess():
    FunctionGuess = input("What is your guess for this " + str(WordLenght) + "letter word? ")
    return FunctionGuess

def CompareFunction(GuessedLetter):
    SecretWord.find(GuessedLetter)
