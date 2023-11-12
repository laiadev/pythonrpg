# PYTHON RPG GAME

# import module :
import cmd
import textwrap
import sys
import os
import time
import random
from player import player
from shop import shop
from expedition import expedition

Player = player()
screen_width = 100


##### Player Setupt #####





##### Screen System #####

def back_option():
    back_option = input("> ")
    check_back_option = False
    while check_back_option == False:
        if back_option.lower() == ("return"):
            title_screen()
        else:
            print("Please enter a valid command.")
            back_option = input("> ")



##### Title Screen #####
def title_screen_selection():
    option = input("> ")
    check_option = False
    while check_option == False:
        if option.lower() == ("load game"):
            load_screen()
            check_option = True
        elif option.lower() == ("new game"):
            new_game()
            check_option = True
        elif option.lower() == ("help"):
            help_screen()
            check_option = True
        elif option.lower() == ("settings"):
            setting_screen()
            check_option = True
        elif option.lower() == ("quit"):
            sys.exit()
            check_option = True
        else:
            print('Please enter a valid command')
            option = input('> ')


def title_screen():
    os.system('cls')
    print("""
+----------------------------------------------------------------------------+
|    ____                  _     _____                                       |
|   / __ \                | |   |  __ \                                      |
|  | |  | | _   _  ___  ___| |_  | |  | | __ _ _ __ ___   __ _  __ _  ___    |
|  | |  | || | | |/ _ \/ __| __| | |  | |/ _` | '_ ` _ \ / _` |/ _` |/ _ \   |
|  | |__| || |_| |  __/\__ \ |_  | |__| | (_| | | | | | | (_| | (_| |  __/   |
|   \___\_\ \__,_|\___||___/\__| |_____/ \__,_|_| |_| |_|\__,_|\__, |\___|   |
|                                                              __/ |         |
|                                                             |___/          |
+----------------------------------------------------------------------------+
|  - Load Game                                                               |
|  - New Game                                                                |
|  - Help                                                                    |
|  - Settings                                                                |
|  - Quit                                                                    |
+----------------------------------------------------------------------------+\n
""")
    title_screen_selection()


def load_screen():
    os.system('cls')
    print("""
+----------------------------------------------------------------------------+
|                                < Load Game >                               |
+----------------------------------------------------------------------------+
|                                                                            |
|                                                                            |
|  - Return                                                                  |
+----------------------------------------------------------------------------+\n
""")
    back_option()


def help_screen():
    os.system('cls')
    print("""
+----------------------------------------------------------------------------+
|                                < Help Menu >                               |
+----------------------------------------------------------------------------+
|                                                                            |
|                                                                            |
|  - Return                                                                  |
+----------------------------------------------------------------------------+\n
""")
    back_option()


def setting_screen():
    os.system('cls')
    print("""
+----------------------------------------------------------------------------+
|                              < Settings Menu >                             |
+----------------------------------------------------------------------------+
|                                                                            |
|                                                                            |
|  - Return                                                                  |
+----------------------------------------------------------------------------+\n
""")
    back_option()


def new_game():
    name_valid = False
    print("\n[min 2|max 16] Choose your Nickname : ")

    # while if name is not valid width
    while (name_valid == False):
        Player.name = input("> ")

        if len(Player.name) >= 2 and len(Player.name) <= 16:
            name_valid = True
        else:
            print("\nPlease enter a valid name width.")

    def new_game_setp2():
        os.system('cls')
        print(f"""
    +----------------------------------------------------------------------------+
    |                               < Avatar Type >                              |
    +----------------------------------------------------------------------------+
    |            Type :           |     Life     |     Shield     |     Mana     |
    |-----------------------------|--------------|----------------|--------------|
    |  - Warrior                  | 200          | 0              | 25           |
    |-----------------------------|--------------|----------------|--------------|
    |  - Archer                   | 120          | 0              | 50           |
    |-----------------------------|--------------|----------------|--------------|
    |  - Mage                     | 80           | 0              | 125          |
    +----------------------------------------------------------------------------+\n
    """)
        Player.type = input("\nChoose your avatar type : ").lower()

        # while if avatar type is not valid
        while (Player.type not in ['warrior', 'archer', 'mage']):
            print("\nPlease enter a valid avatar type.")
            Player.type = input("> ")

    new_game_setp2()

    if Player.type == "warrior":
        Player.life = 200
        Player.shield = 0
        Player.mana = 25

    elif Player.type == "archer":
        Player.life = 120
        Player.shield = 0
        Player.mana = 50

    elif Player.type == "mage":
        Player.life = 80
        Player.shield = 0
        Player.mana = 125

    player_screen()


##### Player Stats Inventory #####
def player_screen():
 while True:
    os.system('cls')
    global Player
    print(f"""   
+----------------------------------------------------------------------------+
|                            < Player Inventory >                            |
+----------------------------------------------------------------------------+
|                                                                            |
|   +-----[ Player Stat ]-----+  +-------------[ Inventory ]-------------+   |
|   | Name : {Player.name} |  |                                       |   |
|   |                         |  |                                       |   |
|   | Type : {Player.type} |  |                                       |   |
|   |                         |  |                                       |   |
|   | Life : {Player.life} |  |                                       |   |
|   |                         |  |                                       |   |
|   | Shield : {Player.shield} |  |                                       |   |
|   |                         |  |                                       |   |
|   | Mana : {Player.mana} |  |                                       |   |
|   |                         |  |                                       |   |
|   | Level : {Player.level} |  |                                       |   |
|   +-------------------------+  +---------------------------------------+   |
|   | Golds : {Player.gold} $ |  |                                       |   |
|   +-------------------------+  +---------------------------------------+   |
|                                                                            |
+----------------------------------------------------------------------------+ 
|                             < Player Actions >                             |
+----------------------------------------------------------------------------+
|  - Expedition                                                              |
|  - Shop                                                                    |
|  - Guild                                                     (Level 5 min) |
|  - Boss                                                     (Level 15 min) |
+----------------------------------------------------------------------------+ \n

""")
    play_option = input("choose an option : ")

    if play_option == "expedition":
        print("expedition")
        Player = expedition(Player)
    elif play_option == "shop":
       Player = shop(Player)
    elif play_option == "guild" and Player.level >= 5:
        print("guild")
    elif play_option == "boss" and Player.level >= 15:
        print("The boss are very hard to kill, are you sure you want to go?")
        boss_valid = False

        # while if bot validation is not valid
        while (boss_valid == False):
            boss_valid_choose = input("[yes/no] > ")
            if boss_valid_choose == "yes":
                print("good luck!")
                boss_valid = True
            elif boss_valid_choose == "no":
                print("wait ...")
                player_screen()
                return
            else:
                print("\nPlease enter a valid option.")

    else:
        print("\nYou dont have the required level to do this.")

##### Launch Title Screen #####
title_screen()
