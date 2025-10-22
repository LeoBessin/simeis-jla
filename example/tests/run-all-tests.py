import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.client import Game
from tests.utils import run_test, delete_json


def create_player():
    fake_name = str(random.randint(0, 2**64 - 1))
    game = Game(fake_name)
    status = game.get(f'/player/{game.player["playerId"]}')
    delete_json(fake_name)
    assert fake_name == status["name"]


def buy_scenario():
    fake_name = str(random.randint(0, 2**64 - 1))
    game = Game(fake_name)
    init_status = game.get(f'/player/{game.player["playerId"]}')
    init_money = init_status["money"]
    game.init_game()
    final_status = game.get(f'/player/{game.player["playerId"]}')
    final_money = final_status["money"]
    print(f"Initial money: {init_money}, final money: {final_money}")
    delete_json(fake_name)
    assert final_money != init_money

def check_cargaison():
    fake_name = str(random.randint(0, 2**64 - 1))
    game = Game(fake_name)
    game.init_game()
    print(game.get(f"/ship/{game.sid}"))
    game.go_mine()
    ress = game.get(f"/ship/{game.sid}")["cargo"]["resources"]
    assert ress != {}
    delete_json(fake_name)

run_test(create_player)

run_test(buy_scenario)

run_test(check_cargaison)
