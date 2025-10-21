import sys
import random
from utils import create_property_based_test


### Example

def addition():
    x = random.randrange(0, 10000)
    y = random.randrange(0, 10000)
    assert x + y > x
    assert x + y > y

create_property_based_test(addition)
