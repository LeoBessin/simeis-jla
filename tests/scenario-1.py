import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from example.client import Game
from utils import create_property_based_test, delete_json


def create_player():
    fake_name = str(random.randint(0, 2**64 - 1))
    game = Game(fake_name)
    status = game.get(f'/player/{game.player["playerId"]}')
    delete_json(fake_name)
    assert fake_name == status["name"]
create_property_based_test(create_player,10)