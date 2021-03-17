import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.RED + Back.WHITE + "What's your name?")
character_name = input(Fore.RED + "Type it in here: ")

print(Fore.RED + Back.WHITE + "How old are you?")
character_age = input(Fore.RED + "Type your age in here here: ")

print(Fore.RED + Back.WHITE + "Where are you from?")
character_whereabouts = input(Fore.RED + "Type the country in here: ")


def isMale():
    Male = input(Fore.RED + Back.WHITE + "You're a male? True or False?: ")
    if (Male == "True"):
        Male_Bool = True
    elif (Male == "False"):
        Male_Bool = False
    if (Male_Bool) == True:
        print(Fore.BLUE + "There was a man named " + character_name + ", ")
        print(Fore.BLUE + "he was " + character_age + ".")
        print(Fore.BLUE + "He likes the name " + character_name + ", ")
        print(Fore.BLUE + "but didn't like being " + character_age + ".")
        print(Fore.BLUE + "He comes from " + character_whereabouts + ",")
    elif (Male_Bool) == False:
        print(Fore.BLUE + "There was a woman named " + character_name + ", ")
        print(Fore.BLUE + "she was " + character_age + ".")
        print(Fore.BLUE + "She likes the name " + character_name + ", ")
        print(Fore.BLUE + "but didn't like being " + character_age + ".")
        print(Fore.BLUE + "She comes from " + character_whereabouts + ",")


def likesCountry():
    print("Do you like your country?")
    likes = input(Fore.RED + Back.WHITE + "True or False?: ")
    if (likes == "True"):
        likes_Bool = True
    elif (likes == "False"):
        likes_Bool = False
    if (likes_Bool) == True:
        print(Fore.BLUE + "and likes the country.")
    elif (likes_Bool) == False:
        print(Fore.BLUE + "and doesn't like the country.")


isMale()

likesCountry()

time.sleep(10)
