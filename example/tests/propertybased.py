import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from tests.utils import create_property_based_test


### Example

def addition():
    x = random.randrange(0, 10000)
    y = random.randrange(0, 10000)
    assert x + y > x
    assert x + y > y

create_property_based_test(addition)
