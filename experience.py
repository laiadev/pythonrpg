def experience(Player, point_experience):
    Player.experience += point_experience
    next_level_experience = Player.level + 60 * 1.4
    if Player.experience > next_level_experience:
        Player.level += 1
        Player.experience = Player.experience - next_level_experience

    return(Player)