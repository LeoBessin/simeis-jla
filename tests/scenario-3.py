import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from example.client import Game
from utils import create_property_based_test, delete_json

def check_Cargaison():
    fake_name = str(random.randint(0, 2**64 - 1))
    game = Game(fake_name)
    game.init_game()
    print(game.get(f"/ship/{game.sid}"))
    game.go_mine()
    ress = game.get(f"/ship/{game.sid}")["cargo"]["resources"]
    assert ress != {}
    delete_json(fake_name)

create_property_based_test(check_Cargaison,1)