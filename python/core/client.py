import sys

from classes.game import Game
from classes.game_threads import GameThread

if __name__ == "__main__":
    name = sys.argv[1]
    game = Game(name)
    game_thread = GameThread()
    for thread in game.threads:
        game_thread.add_thread(thread)
    game_thread.start_threads()


while True:
    ...
