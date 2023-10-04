# Cows and Bulls is a pen and paper code-breaking game usually played between 2 players
# In this, a player tries to guess a secret code number chosen by the second player

import time


print("=================welcome to this game==================")

"""
print("we have two players, the first one have to choose a code formed in 4 digits, then the second player will guess the code ")
print(" Upon making a guess, 2 hints will be provided- Cows and Bulls.")
print("Bulls indicate the number of correct digits in the correct position and cows indicates the number of correct digits in the wrong position")
"""

class joueur :
    def __init__(self,nom,tries):
        self.nom = nom
        self.tries = tries
        
    def name(self):
        return self.nom
    
    def get_tries(self):
        return self.tries
    
    

def getDigits():
    code = []
    print("give a code :")
    for i in range(4):
        code.append(int(input()))
    return code

def guess_code(code,player,tries):
    global buls
    global cows
    i = 0
    while i < tries :
        buls = 0
        cows = 0
        i += 1
        guess = []
        print(f"{player}'s {i} guess :")
        
        guess = [int(input()) for num in range(4)]
        print(f"the guessed code is {guess}")
        
        for j in range(4):
            for h in range(4):
                if code[j]==guess[h] and j==h :
                    buls += 1
                elif code[j]==guess[h] and j != h :
                    cows += 1
                else :
                    pass
        
        if(buls != 4) :
            print("almost got it ! you should try again")
            print(f"results : buls = {buls} | cows = {cows}")
        elif buls == 4 :
            print(f"{player} have won in his {i}th try")
            break
    


play = ['yes','no']
buls = 0
cows = 0

if __name__ == '__main__' :
    choice = str(input("do you want to play :")).lower()
    
    while choice not in play :
        choice = str(input("please give a clear answer :"))
    
    if choice == play[1] :
        print("thanks for your time!")
        exit()
    elif choice == play[0] :
        print("great! let's play now :")
        print("\nloading ...")
        time.sleep(5)
        
    name_1 = str(input("name of the first player :"))
    name_2 = str(input("name of the second player :"))
    
    joueur_1 = joueur(name_1,5)
    joueur_2 = joueur(name_2,5)
    
    print(f"{joueur_1.nom} give a code:")
    code_1 = getDigits()
    print(f"{joueur_2.nom} give a code:")
    code_2 = getDigits()
    
    print(f"\n {joueur_1.nom} have chossed his code, now it's {joueur_2.nom} turn to guess it")
    guess_code(code_1,joueur_2.nom,joueur_2.tries)
    
    print(f"{joueur_2.nom} have chossed his code, now it's {joueur_1.nom} turn to guess it")
    guess_code(code_2,joueur_1.nom,joueur_1.tries)
    