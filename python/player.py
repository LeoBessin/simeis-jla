from utils import create_json


class Player:
    def __init__(self, id=None, key=None, name=None, datalist=None):
        if datalist is not None:
            # Initialize from existing object or dict
            self.id = getattr(datalist, "id", None)
            self.key = getattr(datalist, "key", None)
            self.name = getattr(datalist, "name", None)
            self.lost = getattr(datalist, "lost", False)
            self.money = getattr(datalist, "money", 0)
        else:
            self.id = id
            self.key = key
            self.name = name
            self.lost = False
            self.money = 0
        self.save()

    def get_status(self):
        return (f"id:{self.id}"
                f"key:{self.key}"
                f"name:{self.name}")

    def save(self):
        data = {
            "id": self.id,
            "key": self.key,
            "name": self.name,
            "lost": self.lost,
            "money": self.money,
        }
        create_json(data, self.name)
