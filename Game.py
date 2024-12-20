import base64
import json
import urllib.request


def display_errors(errors):
    for error in errors:
        print('Erreur : ' + error)


class Game:

    def __init__(self, key, code_engine):
        self.token = ''
        self.key = key
        self.code_engine = code_engine
        self.base_url = 'https://tainix.fr/'

    def input(self):
        data = self.request('api/games/start/' + self.key + '/' + self.code_engine)
        self.token = data['token']
        return data['input']

    def output(self, player_data):
        if not player_data['data']:
            display_errors(['Votre tableau de retour doit contenir une cle "data"'])
            return

        player_data = base64.b64encode(json.dumps(player_data).encode('ascii')).decode('ascii')

        data = self.request('api/games/response/' + self.token + '/' + str(player_data))

        print('\n' + data['game_message'] + '\n' + 'Le token de ta Game : ' + self.base_url + 'games/story/' + self.token)

    def request(self, url):
        request = urllib.request.Request(self.base_url + url)
        response = urllib.request.urlopen(request)
        data = json.load(response)

        if not data['success']:
            display_errors(data['errors'])
            return

        return data