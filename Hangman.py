SecretWord = ""
gallow = (200,1,2,3,4,5,6,7,8,9)

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
print(len(SecretWord))
