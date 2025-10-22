import random
import sys
import time
from pathlib import Path

def delete_json(id):
    path = Path(f"{id}.json")
    path.unlink()

def run_test(f):
    start = time.time()
    try:
        f()
    except AssertionError as err:
        print(seed, "test failed")
        print(err)
        sys.exit(1)
    finally:
        end = time.time()
        delta = end - start
        print(f"Test runs in {delta} seconds")
