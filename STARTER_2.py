#!/bin/python
from Game import Game

# Ta key
player_key = 'c047e3e3971f3c057c468172e80f7ce18a81d6e0'
# Le code du challenge
engine_code = 'STARTER_2'


def main():
    game = Game(player_key, engine_code)
    data = game.input()

    # Data du jeu
    print(data)

    # ------- CODE ICI -----------
    res = f"{data["name"]} is in the {data["room"]}."

    response = f"{res}"

    # Permet d'envoyer la reponse du challenge
    game.output({'data': response})


main()