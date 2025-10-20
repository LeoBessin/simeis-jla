import time

from player import Player
from utils import get, read_json, log


class Game:
    def __init__(self, player_name):
        self.player = None
        self.initialize(player_name)
        self.threads = [
            {
                "target": self.server_status_thread,
                "delay": 5
            },
            {
                "target": self.update_player_thread,
                "delay": 10,
            }
        ]

    def update_player_thread(self, delay):
        while True:
            if self.player is not None:
                self.player.update_json()
                log("Player updated")
                log(self.player.get_status())
            time.sleep(delay)

    def get_server_status(self):
        server_status = get("/ping")
        if server_status["ping"] == "pong":
            return "Server is alive"
        else:
            return "Server is dead"


    def server_status_thread(self, delay):
        while True:
            log(self.get_server_status())
            time.sleep(delay)


    def initialize(self, username):
        json_data = read_json(username)
        if json_data:
            self.player = Player(datalist=json_data)
        else:
            player_data = get(f"/player/new/{username}")
            self.player = Player(player_data["playerId"], player_data["key"], username)