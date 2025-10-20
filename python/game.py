from player import Player
from utils import get, read_json


class Game:
    def __init__(self, player_name):
        self.player = None
        self.initialize(player_name)

    def initialize(self, username):
        json_data = read_json(username)
        if json_data:
            print(json_data)
            self.player = Player(datalist=json_data)
        else:
            player_data = get(f"/player/new/{username}")
            self.player = Player(player_data["playerId"], player_data["key"], username)