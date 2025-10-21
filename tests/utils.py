import math
import random
import sys
import time
from pathlib import Path

NB_ITERATIONS_TESTS = 100000

def delete_json(id):
    path = Path(f"{id}.json")
    path.unlink()


def create_property_based_test(f, NB_IT=0):
    regressions = [ ]
    if NB_IT:
        NB_ITERATIONS = NB_IT
    else:
        NB_ITERATIONS = NB_ITERATIONS_TESTS
    start = time.time()
    for i in range(0, NB_ITERATIONS):
        if i < len(regressions):
            seed = regressions[i]
        else:
            seed = random.randrange(0, 2**64)
        random.seed(seed)
        try:
            f()
        except AssertionError as err:
            print(seed, "test failed")
            print(err)
            sys.exit(1)
    end = time.time()
    delta = end - start
    print(f"{NB_ITERATIONS} iterations completed in {delta} seconds")