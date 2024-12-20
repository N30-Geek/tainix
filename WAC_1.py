#!/bin/python
from Game import Game
from functions import calc

# Ta key
player_key = 'c047e3e3971f3c057c468172e80f7ce18a81d6e0'
# Le code du challenge
engine_code = 'WAC_1'


def main():
    game = Game(player_key, engine_code)
    data = game.input()

    # Data du jeu
    print(data)

    # ------- CODE ICI -----------
    members = data["members"]
    results= 0
    
    for m in members:
        results += calc(m)

    response = f"{results:.2f}kg"
    
    # Permet d'envoyer la reponse du challenge
    game.output({'data': response})


main()