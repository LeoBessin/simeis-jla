import urllib
import urllib.request
import json
import os
from dotenv import load_dotenv

load_dotenv()

PORT=os.getenv('PORT')
SERVER_URL=os.getenv('SERVER_URL')
URL=f"http://{SERVER_URL}:{PORT}"

class SimeisError(Exception):
    pass

def get(path, **qry):
        tail = ""
        if len(qry) > 0:
            tail += "?"
            tail += "&".join([
                "{}={}".format(k, urllib.parse.quote(v)) for k, v in qry.items()
            ])

        qry = f"{URL}{path}{tail}"
        reply = urllib.request.urlopen(qry, timeout=1)

        data = json.loads(reply.read().decode())
        err = data.pop("error")
        if err != "ok":
            raise SimeisError(err)

        return data

def create_json(data, filename):
    with open(f"./data/{filename}.json", "w") as f:
        json.dump(data, f)

def read_json(filename):
    try:
        with open(f"./data/{filename}.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None