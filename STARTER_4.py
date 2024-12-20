#!/bin/python
from Game import Game

# Ta key
player_key = 'c047e3e3971f3c057c468172e80f7ce18a81d6e0'
# Le code du challenge
engine_code = 'STARTER_4'


def main():
    game = Game(player_key, engine_code)
    data = game.input()

    # Data du jeu
    print(data)

    # ------- CODE ICI -----------
    stop = data["stop"]
    sum = 0
    counter = 1

    while counter < stop:
        sum += counter
        counter +=1
        
        if counter == stop:
            break
        
        
    response = f"{sum}"

    # Permet d'envoyer la reponse du challenge
    game.output({'data': response})


main()