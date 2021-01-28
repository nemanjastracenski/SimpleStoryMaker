import time
print("What's your name?")
character_name = input("Type it in here: ")
print("How old are you?")
character_age = input("Type your age in here here: ")
def isMale():
    Male = input("You're a male? True or False? ")
    if (Male == "True"):
        Male_Bool = True
    elif (Male == "False"):
        Male_Bool = False
    if (Male_Bool) == True:
        print("There was a man named " + character_name + ", ")
        print("he was " + character_age + ".")
        print("He likes the name " + character_name + ", ")
        print("but didn't like being " + character_age + ".")
    elif(Male_Bool) == False:
        print("There was a woman named " + character_name + ", ")
        print("she was " + character_age + ".")
        print("She likes the name " + character_name + ", ")
        print("but didn't like being " + character_age + ".")
isMale()
time.sleep(10)
