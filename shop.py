def heal(Player):
    print("""
    +---------------------------------------------------------------+
    |                  <     Shop Heal    >                         |
    +---------------------------------------------------------------+
    | Item           | Health Points (HP) | Price ( $ )             |
    +---------------------------------------------------------------+
    | name1          | 30 PV              | 10                      |
    | name2          | 60 PV              | 25                      |
    | name3          | 90 PV              | 30                      |
    | Return         |                    |                         |
    +---------------------------------------------------------------+
    """)

    check_option = False

    while check_option == False:
        gold = Player.gold
        option = input('> ').lower()
        if option == ("name1"):
            if int(gold) >= 10:
                Player.gold -= 10
                Player.life += 30
                print('You have gained 30 HP')
            else:
                print("You don't have 10 $")

        elif option == ("name2"):
            if int(gold) >= 20:
                Player.gold -= 20
                Player.life += 60
                print('You have gained 60 HP')
            else:
                print("You don't have 20 $")

        elif option == ("name3"):
            if int(gold) >= 30:
                Player.gold -= 30
                Player.life += 90
                print('You have gained 90 HP')
            else:
                print("You don't have 30 $")

        elif option == ("return"):
            print("""
    +----------------------------------------------------------------------------+ 
    |                              <     Shop     >                              |
    +----------------------------------------------------------------------------+
    |  - Heal                                                                    |
    |  - Mana                                                                    |
    |  - Shield                                                                  |
    |  - Quit                                                                    |
    +----------------------------------------------------------------------------+ """)
            check_option = True
            return (Player)

        else:
            print('Please enter a valid command')

    return (Player)
def mana(Player):
    print("""
    +---------------------------------------------------------------+
    |                  <     Shop Mana    >                         |
    +---------------------------------------------------------------+
    | Item           | Mana Points (MP)   | Price ( $ )             |
    +---------------------------------------------------------------+
    | name1          | 30 MP              | 10                      |
    | name2          | 60 MP              | 25                      |
    | name3          | 90 MP              | 30                      |
    | Return         |                    |                         |
    +---------------------------------------------------------------+
        """)

    check_option = False

    while check_option == False:
        gold = Player.gold
        option = input('> ').lower()
        if option == ("name1"):
            if int(gold) >= 10:
                Player.gold -= 10
                Player.mana += 30
                print('You have gained 30 MP')
            else:
                print("You don't have 10 $")

        elif option == ("name2"):
            if int(gold) >= 20:
                Player.gold -= 20
                Player.mana += 60
                print('You have gained 60 MP')
            else:
                print("You don't have 20 $")

        elif option == ("name3"):
            if int(gold) >= 30:
                Player.gold -= 30
                Player.mana += 90
                print('You have gained 90 MP')
            else:
                print("You don't have 30 $")

        elif option == ("return"):
            print("""
+----------------------------------------------------------------------------+ 
|                              <     Shop     >                              |
+----------------------------------------------------------------------------+
|  - Heal                                                                    |
|  - Mana                                                                    |
|  - Shield                                                                  |
|  - Quit                                                                    |
+----------------------------------------------------------------------------+ """)
            check_option = True
            return (Player)

        else:
            print('Please enter a valid command')

    return (Player)
def shield(Player):
    print("""
    +---------------------------------------------------------------+
    |                  <     Shop Shield    >                       |
    +---------------------------------------------------------------+
    | Item           | Shield             | Price ( $ )             |
    +---------------------------------------------------------------+
    | name1          | 30                 | 10                      |
    | name2          | 60                 | 25                      |
    | name3          | 90                 | 30                      |
    | Return         |                    |                         |
    +---------------------------------------------------------------+
            """)

    check_option = False

    while check_option == False:
        gold = Player.gold
        option = input('> ').lower()
        if option == ("name1"):
            if int(gold) >= 10:
                Player.gold -= 10
                Player.shield += 30
                print('You have gained 30 shield')
            else:
                print("You don't have 10 $")

        elif option == ("name2"):
            if int(gold) >= 20:
                Player.gold -= 20
                Player.shield += 60
                print('You have gained 60 shield')
            else:
                print("You don't have 20 $")

        elif option == ("name3"):
            if int(gold) >= 30:
                Player.gold -= 30
                Player.shield += 90
                print('You have gained 90 shield')
            else:
                print("You don't have 30 $")

        elif option == ("return"):
            print("""
    +----------------------------------------------------------------------------+ 
    |                              <     Shop     >                              |
    +----------------------------------------------------------------------------+
    |  - Heal                                                                    |
    |  - Mana                                                                    |
    |  - Shield                                                                  |
    |  - Quit                                                                    |
    +----------------------------------------------------------------------------+ """)
            check_option = True
            return (Player)

        else:
            print('Please enter a valid command')
    return (Player)


def shop(Player):
    print("""
+----------------------------------------------------------------------------+ 
|                              <     Shop     >                              |
+----------------------------------------------------------------------------+
|  - Heal                                                                    |
|  - Mana                                                                    |
|  - Shield                                                                  |
|  - Quit                                                                    |
+----------------------------------------------------------------------------+ """)

    check_option = False

    while check_option == False:
        option = input('> ').lower()
        if option == ("heal"):
            heal(Player)
        elif option == ("mana"):
            mana(Player)
        elif option == ("shield"):
            shield(Player)
        elif option == ("quit"):
            return(Player)
            check_option = True
        else:
            print('Please enter a valid command')

    return(Player)