import urllib.request
import json
import os
from dotenv import load_dotenv

load_dotenv()

PORT=os.getenv('PORT')
SERVER_URL=os.getenv('SERVER_URL')
URL=f"http://{SERVER_URL}:{PORT}"

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

print(get("/ping"))