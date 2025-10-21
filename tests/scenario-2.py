import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from example.client import Game
from utils import create_property_based_test, delete_json


def buy_scenario():
    fake_name = str(random.randint(0, 2**64 - 1))
    game = Game(fake_name)
    initStatus = game.get(f'/player/{game.player["playerId"]}')
    initMoney = initStatus["money"]
    game.init_game()
    finalStatus = game.get(f'/player/{game.player["playerId"]}')
    finalMoney = finalStatus["money"]
    print(f"Initial money: {initMoney}, final money: {finalMoney}")
    delete_json(fake_name)
    assert finalMoney != initMoney
create_property_based_test(buy_scenario,10)