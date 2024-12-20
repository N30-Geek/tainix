#!/bin/python
from Game import Game

# Ta key
player_key = 'c047e3e3971f3c057c468172e80f7ce18a81d6e0'
# Le code du challenge
engine_code = 'STARTER_6'


def main():
    game = Game(player_key, engine_code)
    data = game.input()

    # Data du jeu
    print(data)

    # ------- CODE ICI -----------
    values = data["values"]

    
    def diviseur_trois(values):
        for  v in values:
            output = []
            if v%3 == 0:
                output.append(str(v))
                
        return "-".join(output)

    response = diviseur_trois(values)
    
    # Permet d'envoyer la reponse du challenge
    game.output({'data': response})


main()