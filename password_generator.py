import random
import string

def generate_password(min_length, numbers, special_characters):
    x=0
    password=""


    while x!=min_length:
        password+= random.choice(string.ascii_letters)
        x+=1

        if x!=min_length and numbers==True:
            password+= str(random.randint(0,9))
            x+=1

        if x!=min_length and special_characters==True:
            password+= random.choice("!-_?*()=+~@#$%^&'*")
            x+=1

    return password


print("Welcome to the Password Generator\nBefore generating your password, we would like to ask you a couple of questions")
size= int(input("What size password would you like?"))
numbers= input("Yes or No, would you like Numbers in your password?").lower() =='yes'
characters= input("Yes or No, would you like Special Characters (Ex: $#%^&*@) in your password?").lower() =='yes'
print("Here is your new passowrd: "+ generate_password(size, numbers, characters))