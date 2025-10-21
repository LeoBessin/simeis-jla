from utils import create_property_based_test
from example.tests.scenario_1 import create_player
from scenario_2 import buy_scenario
from scenario_3 import check_Cargaison

create_property_based_test(create_player, 10)

create_property_based_test(buy_scenario, 10)

create_property_based_test(check_Cargaison, 1)
