import random

from experience import experience
def losehp(Player, hpless):
    Playerlife = Player.life

    if Playerlife - hpless > 0:
        Player.life -= hpless
        point_experience = int(random.randint(10,30))
        print(f"Vous venez de récuper {point_experience} point experience et vous avez perdu {hpless} HP")
        Player = experience(Player, point_experience)
    else:
        Player.life = 0
        print("Vous avez perdu votre combat vous etre à 0HP")
    return(Player)
def losemana(Player, manaless):
    Playermana = Player.life

    if Playermana - manaless > 0:
        Player.mana -= manaless
        point_experience = int(random.randint(10,30))
        print(f"Vous venez de récuper {point_experience} point experience et vous avez perdu {manaless} mana")
        Player = experience(Player, point_experience)
    else:
        Player.life = 0
        print("Vous avez perdu votre combat vous etre à 0HP")
    return(Player)

def expedition(Player):
    Player = losehp(Player, 30)
    return(Player)