import time

from classes.player import Player
from core.utils import get, read_json, log


class Game:
    def __init__(self, player_name):
        self.player = None
        self.initialize(player_name)
        self.threads = [
            # {
            #     "target": self.server_status_thread,
            #     "delay": 5
            # },
            {
                "target": self.update_player_thread,
                "delay": 10,
            },
        ]

    def buy_ship(self, station_id, ship_id):
        err = get(f"/station/{station_id}/shipyard/buy/{ship_id}")
        if err:
            print(err)
            return False
        else:
            return True


    def update_player_thread(self, delay):
        while True:
            if self.player is not None:
                self.player.update_json()
                log("Player updated")
                log(self.player.get_status())
            time.sleep(delay)

    def buy_ship(self):
        station_ids = self.player.stations.keys()
        first_station_id = list(station_ids)[0]
        if first_station_id is not None:
            ships = get(f"/station/{first_station_id}/shipyard/list")
            print(ships)


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