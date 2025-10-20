import threading
import time

from player import Player
from utils import get, read_json


class Game:
    def __init__(self, player_name):
        self.player = None
        self.initialize(player_name)
        self.threads = []
        self.status_delay = 5


    def status_thread(self, delay):
        while True:
            print(self.player.get_status())
            time.sleep(delay)

    def initialize(self, username):
        json_data = read_json(username)
        if json_data:
            self.player = Player(datalist=json_data)
        else:
            player_data = get(f"/player/new/{username}")
            self.player = Player(player_data["playerId"], player_data["key"], username)

    def initialize_thread(self):
        t = threading.Thread(target=self.status_thread, args=(self.status_delay,))
        self.threads.append(t)

    def start_threads(self):
        for thread in self.threads:
            thread.start()