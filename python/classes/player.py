from core.utils import create_json, get, set_player_key


class Player:
    def __init__(self, id=None, key=None, name=None, datalist=None):
        if datalist is not None:
            self.id = datalist["id"]
            self.key = datalist["key"]
            self.name = datalist["name"]
            self.lost = datalist["lost"]
            self.money = datalist["money"]
            self.costs = datalist["costs"]
            self.ships = datalist["ships"]
            self.stations = datalist["stations"]
        else:
            self.id = id
            self.key = key
            self.name = name
            self.lost = False
            self.money = 0
            self.costs = 0
            self.ships = []
            self.stations = {}
        set_player_key(self.key)
        self.update_json()

    def get_status(self):
        return (
                "Player (\n"
                f"  id:{self.id}\n"
                f"  key:{self.key}\n"
                f"  name:{self.name}\n"
                f"  lost:{self.lost}\n"
                f"  money:{self.money}\n"
                f"  costs:{self.costs}\n"
                f"  ships:{self.ships}\n"
                f"  stations:{self.stations}\n"
                ")"
            )

    def update_json(self):
        player_data = get(f"/player/{self.id}")
        self.money = player_data["money"]
        self.costs = player_data["costs"]
        self.ships = player_data["ships"]
        self.stations = player_data["stations"]
        self.save()

    def save(self):
        data = {
            "id": self.id,
            "key": self.key,
            "name": self.name,
            "lost": self.lost,
            "money": self.money,
            "costs": self.costs,
            "ships": self.ships,
            "stations": self.stations,
        }
        create_json(data, self.name)
