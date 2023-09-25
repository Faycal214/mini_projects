import random
import string
import time
import getpass


def check_password_strength():
    
    password = str(input("enter your password :"))
    
    #this is when the user wants the programme to generate him a password instead
    """
    taille=int(input("give the length of your password:"))
    
    while(taille<=0):
        print("invalid value, please enter another one:")
        taille=int(input())
    
    special = string.punctuation
    lower_letter = string.ascii_lowercase
    upper_letter = string.ascii_uppercase
    digit = string.digits
    
    caractere = special + lower_letter + upper_letter + digit
    password =""
    
    for i in range(taille):
        password += random.choice(caractere)
    
    print(f"the password generated is {password}")
    """
    
    lower_count = upper_count = digit_count = special_count = space_count = 0
    strength = 0
    remark =""
    
    for char in list(password) :
        if char in string.punctuation :
            special_count += 1
        elif char == " " :
            space_count += 1
        elif char in string.ascii_lowercase :
            lower_count += 1
        elif char in string.ascii_uppercase :
            upper_count += 1
        elif char in string.digits :
            digit_count += 1
    
    if special_count >= 1 :
        strength += 1
    if lower_count >= 1 :
        strength += 1
    if space_count >= 1 :
        strength += 1
    if upper_count >= 1 :
        strength += 1
    if digit_count >= 1 :
        strength += 1
    
    if strength == 1 :
        remark = ("it's a very bad password ,please change it as soon as possible")
    elif strength == 2 :
        remark = ("that's a weak password, you should consider change it")
    elif strength == 3 :
        remark = ("your password is OK but it can be improved ")
    elif strength == 4 :
        remark = ("your password is hard to guess , but you could make it even more secure")
    elif strength == 5 :
        remark = ("now that's one hell of a strong password !!! "
              "hackers don't have a chance guessing that password")
    
    print("your password has :")
    print(f"{lower_count} lowercase letters")
    print(f"{upper_count} uppercase letters")
    print(f"{digit_count} digits")
    print(f"{special_count} special caracters")
    print(f"password score : {strength}")
    print(f"remarks : {remark}")


def check_pswd():
    valid = True
    
    choice = input("do you want to check your password's strength (yes/no) :")
    
    while valid :
        if choice.lower()=='yes':
            return True
        elif choice.lower()=='no':
            print("exiting...")
            time.sleep(3)
            return False
        else :
            print("invalid input, please try again \n")
            exit()


if __name__ == '__main__':
    print("============welcome to password strength geneartor==============")
    check_pwd = check_pswd()
    while check_pwd :
        check_password_strength()
        check_pwd = check_pswd()

